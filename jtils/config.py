import os
import inspect
import hydra
from hydra import compose, initialize
from omegaconf import OmegaConf
import omegaconf

from jtils.files import get_directory, get_filename

def clear_hydra():
    ' GlobalHydra is already initialized, call GlobalHydra.instance().clear() if you want to re-initialize'
    hydra.core.global_hydra.GlobalHydra.instance().clear()
    
def load_config(config_filepath):
    fdir = get_directory(config_filepath)
    fdir = os.path.relpath(fdir, start = os.curdir)
    
    fname = get_filename(config_filepath, extension=False)
    
    clear_hydra()
    initialize(config_path=fdir)
    cfg = compose(config_name=fname)
    
    return cfg

def get_value(key : str, cfg: omegaconf.dictconfig.DictConfig, recursive: bool = False) -> object:
    """
    Get value in config corresponting to key
    """
    if key in cfg:
        return cfg[key]
    elif recursive:
        for k, v in cfg.items():
            if isinstance(v, omegaconf.dictconfig.DictConfig):
                out = get_value(key, v)
                if out is not None:
                    return out

def config_eval(fnc):
    """
    Decorator
    
    Swap inputs for function with a dictionary of inputs
    
    Inspect function for named arguments and look them up in dictionary/ config. 
    Then evaluate function using these inputs.
    
    """
    def fn(cfg):
        fn_input = {}
        fn_sig = inspect.signature(fnc)
        for k,v in fn_sig.parameters.items():
            out = get_value(k, cfg)
            if out is not None:
                fn_input[k] = out
            else:
                fn_input[k] = v.default
        return fnc(**fn_input)
    return fn
        
                    