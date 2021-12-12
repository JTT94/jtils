from pathlib import Path

def get_current_directory() -> str:
    return get_directory('__file__')

def get_directory(filepath :str) -> str:
    path = Path(filepath).parent.absolute()
    return str(path)

def get_filename(filepath : str, extension : bool = True) -> str:
    if extension:
        path = Path(filepath).name
    else:
        path = Path(filepath).stem
    return str(path)
    
def get_file_extension(filepath : str) -> str:
    path = Path(filepath).suffix
    return str(path)
