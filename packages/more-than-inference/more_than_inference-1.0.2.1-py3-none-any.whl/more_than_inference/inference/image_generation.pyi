import builtins
import multiprocessing.connection
from abc import abstractmethod
from pathlib import Path
from typing import Any, List, Union

from pydantic import BaseModel

class ImageGenerationInput(BaseModel):
    task_id: str
    models: str
    prompt: str
    negative_prompt: str
    input_images: List[Union[Path, str]]
    output_directory: Union[Path, str]
    steps: int
    seed: int
    generation_count: int

    def __init__(self, 
                 task_id: str = ..., 
                 models:str=...,
                 prompt: str = ..., 
                 negative_prompt: str = ..., 
                 input_images: List[Union[Path, str]] = ..., 
                 output_directory: Union[Path, str] = ..., 
                 steps: int = ..., 
                 seed: int = ..., 
                 generation_count: int = ...
                 ) -> None: ...

class ImageGenerationOutput(BaseModel):
    output_images: List[Union[Path, str]]
    trace_back_info: str
    task_finished: bool

    def __init__(self, 
                 output_images: List[Union[Path, str]] = ..., 
                 trace_back_info: str = ..., 
                 task_finished: bool = ...
                 ) -> None: ...

class ImageGenerationBase:
    def store_args(self:"ImageGenerationBase", args:Any=None, unknown_args:Any=None) -> None: ...
    @classmethod
    def print_inferences(cls:type["ImageGenerationBase"]): ...
    @classmethod
    def get_inference(cls:type["ImageGenerationBase"], name:builtins.str=None, module:builtins.str=None): ...
    @abstractmethod
    def load_model(self:"ImageGenerationBase", *args, **kwargs): ...
    @abstractmethod
    def unload_model(self:"ImageGenerationBase", *args, **kwargs): ...
    @abstractmethod
    def preprocess(self:"ImageGenerationBase", data: ImageGenerationInput, *args, **kwargs)->ImageGenerationInput: ...
    @abstractmethod
    def postprocess(self:"ImageGenerationBase", data: ImageGenerationOutput, *args, **kwargs)->ImageGenerationOutput: ...
    @abstractmethod
    def predict(self:"ImageGenerationBase", data: ImageGenerationInput, *args, **kwargs)->ImageGenerationOutput: ...
    def run(self:"ImageGenerationBase", data: Any, *args, **kwargs): ...
    def run_async(self: "ImageGenerationBase", pipe: multiprocessing.connection.Connection): ...
    def run_pipeline(self: "ImageGenerationBase", pipe: multiprocessing.connection.Connection): ...

def image_path_to_b64s(paths:Union[Path,List[Path]])->Union[str,List[str]]: ...
def image_b64s_to_path(strs:Union[str,List[str]], base:Path)->Union[Path,List[Path]]: ...