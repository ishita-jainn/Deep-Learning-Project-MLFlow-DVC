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

@dataclass(frozen = True)
class TrainingConfig:
    root_dir : Path
    trained_model_path : Path
    updated_base_model_path : Path
    training_data : Path
    params_epochs: int
    params_batch_size : int
    params_is_augmentation : bool
    params_image_size : list

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model : Path
    training_data : Path
    all_params : dict
    mlflow_uri : str
    params_image_size : list
    params_batch_size : int

