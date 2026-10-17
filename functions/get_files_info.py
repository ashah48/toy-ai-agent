# functions/get_files_info.py
import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    if directory == ".":
        result = "Result for current directory: \n"
    else:
        result = f"Result for '{directory}' directory \n"

    try:
        abs_path_wdir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path_wdir, directory))
    
        # Check if the target directory path is
        # within the absolute working directory path
        valid_target_dir = os.path.commonpath([abs_path_wdir, target_dir]) == abs_path_wdir
        if not valid_target_dir:
            result += f' Error: Cannot list "{directory}" as it is outside the permitted working directory \n'
            return result
    
        # Check that target directory is actually a directory
        if not os.path.isdir(target_dir):
            result += f' Error: "{directory}" is not a directory \n'
            return result
        
        # target directory is valid
        result += format_dir_listing(target_dir)
        return result
    
    except Exception as e:
        return f'Error: {e}'

# Helper function for formatting file listing 
def format_dir_listing(target_dir: str) -> str:
    dir_listing = os.listdir(target_dir)
    py_files = []
    dirs = []
    jsons = []
    markdowns = []
    txts = []
    for item in dir_listing:
        entry_path = os.path.join(target_dir, item)
        if entry_path.lower().endswith(".py"):
            py_files.append(item)
        if entry_path.lower().endswith(".json"):
            jsons.append(item)
        if entry_path.lower().endswith(".md"):
            markdowns.append(item)
        if entry_path.lower().endswith(".txt"):
            txts.append(item)
        if os.path.isdir(entry_path):
            dirs.append(item)

    result = ""
    for file in py_files:
        entry_path = os.path.join(target_dir, file)
        result += f'  - {file}: file_size={os.path.getsize(entry_path)} bytes, is_dir=False \n'

    for file in jsons:
        entry_path = os.path.join(target_dir, file)
        result += f'  - {file}: file_size={os.path.getsize(entry_path)} bytes, is_dir=False \n'

    for file in markdowns:
        entry_path = os.path.join(target_dir, file)
        result += f'  - {file}: file_size={os.path.getsize(entry_path)} bytes, is_dir=False \n'

    for file in txts:
        entry_path = os.path.join(target_dir, file)
        result += f'  - {file}: file_size={os.path.getsize(entry_path)} bytes, is_dir=False \n'

    for directory in dirs:
        entry_path = os.path.join(target_dir, directory)
        result += f'  - {directory}: file_size={os.path.getsize(entry_path)} bytes, is_dir=True \n'

    return result