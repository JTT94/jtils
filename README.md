# jtils


## Install from github
`pip install git+https://github.com/JTT94/jtils.git`

## Add environment to Jupyter kernel
`python -m ipykernel install --user --name=jtils`

## Config management with Hydra 

- Load config
```
    
    from jtils.config import get_value, load_config, config_eval, clear_hydra
    from jtils.filepaths import get_directory, get_filename


    config_path = '../configs/mnist.yaml'

    cfg = load_config(config_path)

```

- Evaluate function using config inputs

```
    config_eval(fn)(cfg)
```

## git
```
    from jtils.git import git_push
    git_push()

```