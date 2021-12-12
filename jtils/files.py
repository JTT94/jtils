from pathlib import Path
import os
import errno
import zipfile

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


def makedir_exist_ok(dirpath):
    """
    Python2 support for os.makedirs(.., exist_ok=True)
    """
    try:
        os.makedirs(dirpath)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise

def extract_from_zip(zip_file, unzip_dir):
    with zipfile.ZipFile(zip_file, "r") as f:
        f.extractall(unzip_dir)