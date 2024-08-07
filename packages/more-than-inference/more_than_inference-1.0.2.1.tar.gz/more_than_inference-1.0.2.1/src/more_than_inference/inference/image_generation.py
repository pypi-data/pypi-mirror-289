import base64
import multiprocessing.connection
import uuid
from pathlib import Path
from typing import List, Union

from pydantic import BaseModel, Field

from more_than_inference.inference.meta import ArgParserMixin, InferMixin, MetaInference, ModuleMixin, RuntimeMixin
from more_than_inference.utils.register import META


class ImageGenerationInput(BaseModel):
    task_id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    models: str = "{}"
    prompt: str = ""
    negative_prompt: str = ""
    input_images: List[Union[Path, str]] = []
    output_directory: Union[Path, str] = None
    steps: int = 20
    seed: int = -1
    generation_count: int = 1


class ImageGenerationOutput(BaseModel):
    output_images: List[Union[Path, str]] = []
    trace_back_info: str = ""
    task_finished: bool = False


def image_path_to_b64s(paths: Union[Path, List[Path]]) -> Union[str, List[str]]:
    def path_to_b64(path: Path) -> str:
        with open(path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    if isinstance(paths, list):
        return [path_to_b64(path) for path in paths]
    else:
        return path_to_b64(paths)


def image_b64s_to_path(strs: Union[str, List[str]], base: Path) -> Union[Path, List[Path]]:
    def b64_to_image(b64_str: str, file_path: Path):
        image_data = base64.b64decode(b64_str)
        with open(file_path, 'wb') as file:
            file.write(image_data)

    if isinstance(strs, list):
        paths = []
        for idx, b64_str in enumerate(strs):
            file_path = base.parent / f"{base.stem}_{idx+1}.png"
            b64_to_image(b64_str, file_path)
            paths.append(file_path)
        return paths
    else:
        file_path = base.with_suffix('.png')
        b64_to_image(strs, file_path)
        return file_path


class RunAsyncMixin:
    def run_async(self: RuntimeMixin, pipe: multiprocessing.connection.Connection):
        inputs: ImageGenerationInput = pipe.recv()
        outputs: ImageGenerationOutput = self.run(data=inputs)
        pipe.send(outputs)


class RunPipelineMixin:
    def run_pipeline(self: RuntimeMixin, pipe: multiprocessing.connection.Connection): ...


@META.regist(name="ImageGeneration")
class ImageGenerationBase(ArgParserMixin,
                          ModuleMixin,
                          InferMixin,
                          RuntimeMixin,
                          RunAsyncMixin,
                          RunPipelineMixin,
                          metaclass=MetaInference):
    ...
