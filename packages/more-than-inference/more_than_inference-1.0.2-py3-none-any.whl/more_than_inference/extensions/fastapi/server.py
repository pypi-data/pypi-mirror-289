import base64
import multiprocessing.connection
import tempfile
from multiprocessing import shared_memory
from pathlib import Path
from typing import Callable, Dict, List

import cv2
import numpy as np
from loguru import logger
from pydantic import BaseModel
from requests import Session

from more_than_inference.extensions.fastapi.server_base import FastServer
from more_than_inference.inference.image_generation import (ImageGenerationInput, ImageGenerationOutput, image_b64s_to_path,
                                                            image_path_to_b64s)
from more_than_inference.utils.register import META


class PredictRequest(BaseModel):
    images: List[str]
    image_type: str


class Server(FastServer):
    async def object_detection(self, images, image_type) -> Dict:
        imgs = []
        if image_type == 'url':
            for image in images:
                with Session() as client:
                    resp = await client.get(image)
                    byte_content = await resp.read()
                image = np.asarray(bytearray(byte_content), dtype="uint8")
                image = cv2.imdecode(image, cv2.IMREAD_COLOR)
                imgs.append(image)
        elif image_type == 'image':     # act前端 base64
            for image in images:
                image_data = base64.b64decode(image)
                image_array = np.frombuffer(image_data, np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                imgs.append(image)
        else:
            raise ValueError(f'image_type is invalid!')

        result = self._callback_func(imgs)
        logger.info(f"RET: {result}")
        return result

    @META.regist_server("ASYNC_OD")
    def run_async_object_detection(self, pipe: multiprocessing.connection.Connection):
        def processing_async(imgs: list[np.ndarray]) -> dict:
            shms: list[shared_memory.SharedMemory] = []
            sends: List[tuple] = []
            for img in imgs:
                shm = shared_memory.SharedMemory(create=True, size=img.nbytes)
                shared_arr = np.ndarray(img.shape, dtype=img.dtype, buffer=shm.buf)
                np.copyto(shared_arr, img)
                shms.append(shm)
                sends.append((shm.name, img.shape, img.dtype))

            pipe.send(sends)
            result = pipe.recv()
            for shm in shms:
                shm.close()
                shm.unlink()
            return result
        return processing_async

    async def image_generation(self, ig_input: ImageGenerationInput) -> ImageGenerationOutput:
        ig_output: ImageGenerationOutput = self._callback_func(ig_input)
        logger.info(f"IG_STATUS: {ig_output.task_finished}")
        return ig_output

    @META.regist_server("ASYNC_IG")
    def run_async_image_generation(self, pipe: multiprocessing.connection.Connection):
        def processing_async(ig_input: ImageGenerationInput) -> ImageGenerationOutput:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dir_path = Path(temp_dir)
                base_path = temp_dir_path / "input"
                ig_input.input_images = image_b64s_to_path(ig_input.input_images, base_path)
                ig_input.output_directory = temp_dir_path
                pipe.send(ig_input)
                ig_output: ImageGenerationOutput = pipe.recv()
                ig_output.output_images = image_path_to_b64s(ig_output.output_images)
                return ig_output
        return processing_async

    def _setup_routes(self):
        super()._setup_routes()

        @self.app.post("/forward_ig")
        @self.app.get("/forward_ig")
        async def forward_ig(request: ImageGenerationInput):
            return await self.image_generation(request)

        @self.app.post("/predict_od")
        @self.app.get("/predict_od")
        async def predict_od(request: PredictRequest):
            return await self.object_detection(request.images, request.image_type)

        # add act service route
        @self.app.post("/autotable/predict")
        @self.app.get("/autotable/predict")
        async def act(request: PredictRequest):
            return await self.object_detection(request.images, request.image_type)

    def run(self, callback: Callable):
        self._callback_func = callback
        super().run()
