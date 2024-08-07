import multiprocessing.connection
from multiprocessing import shared_memory
from typing import List

import numpy as np

from more_than_inference.inference.meta import ArgParserMixin, InferMixin, MetaInference, ModuleMixin, RuntimeMixin
from more_than_inference.utils.register import META


class RunBatchImagesAsyncMixin:
    def run_async(self: RuntimeMixin, pipe: multiprocessing.connection.Connection):
        kwdict, *pipe_inputs = pipe.recv()
        imgs = []
        for pipe_image in pipe_inputs:
            shm_name, shm_shape, shm_dtype = pipe_image
            existing_shm = shared_memory.SharedMemory(name=shm_name)
            imgs.append(np.ndarray(shm_shape, dtype=shm_dtype, buffer=existing_shm.buf))
            existing_shm.close()
        rsts = self.run(imgs, **kwdict)
        pipe.send(rsts)


@META.regist(name="Detection")
class DetectionBase(ArgParserMixin,
                    ModuleMixin,
                    InferMixin,
                    RuntimeMixin,
                    RunBatchImagesAsyncMixin,
                    metaclass=MetaInference):
    ...


def run_batch_async_detection(pipe: multiprocessing.connection.Connection):
    def processing_async(imgs: list[np.ndarray], kwdict: dict = None) -> dict:
        shms: list[shared_memory.SharedMemory] = []
        sends: List[tuple] = [kwdict or {}]
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
