# Deep-Learning-Project-MLFlow-DVC

## Workflows

1. Update config.yaml
2. Update secrets.yaml    [Optional-passwords]
3. Update params.yaml
4. Update entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/ishita-jainn/Deep-Learning-Project-MLFlow-DVC
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnn-env python=3.9 -y
```

```bash
conda activate cnn-env
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag




### dagshub
MLFLOW tracking URI : https://dagshub.com/ishita-jainn/Deep-Learning-Project-MLFlow-DVC.mlflow/