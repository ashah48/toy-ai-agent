# functions/get_file_content.py
import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path_wdir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wdir, file_path))
    
        # Check if the target file path is
        # within the absolute working directory path
        valid_target_file = os.path.commonpath([abs_path_wdir, target_file]) == abs_path_wdir
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory \n'
    
        # Check that target directory is actually a file
        if not os.path.isfile(target_file):
            return f'Error: file not found or is not a regular file "{file_path}"\n'

        # Target file is valid
        return read_file(target_file)

    except Exception as e:
        return f'Error: {e}'

# Helper function
def read_file(entry_path: str) -> str:
    with open(entry_path, "r") as f:
        file_content_str = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS:
        if f.read(1):
            file_content_str += f'[...File "{entry_path}" truncated at {MAX_CHARS} characters]'
        return file_content_str