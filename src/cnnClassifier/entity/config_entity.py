#Entity : return type of any function

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)   #dataclass is a deocrator that can be assignd to any function to make it an entity. Its  not exactly a class but behaves like a class
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path

@dataclass(frozen=True) #frozen=true means i dont want to add anything else in this
class PrepareBaseModelConfig:
    root_dir:Path
    base_model_path:Path
    updated_base_model_path:Path
    params_image_size: list
    params_learning_rate: float
    params_classes: int
    params_weights: str
    params_include_top: bool