# functions/run_python_file.py
import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
    ) -> str:
    try:
        abs_path_wdir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wdir, file_path))

        # Check if the target file path is
        # within the absolute working directory path
        valid_target_file = os.path.commonpath([abs_path_wdir, target_file]) == abs_path_wdir
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory \n'
    
        # Check if target file is actually a directory
        if os.path.isdir(target_file):
            return f'Error: Cannot execute "{file_path}" as it is a directory'

        # Allow new files, but reject an existing path that is not a regular file
        if not (os.path.exists(target_file) and os.path.isfile(target_file)):
            return f'Error: "{file_path}" does not exist or is not a regular file \n'

        # Check that the target file is a .py
        if not target_file.lower().endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Run a subprocess
        command = ["python", target_file, *(args or [])]
        result = subprocess.run(command, cwd=abs_path_wdir, capture_output=True, 
        text=True, timeout=30)
        output_str = ""
        if result.returncode != 0:
            output_str += "Process exited with code X \n"
        if result.stdout is None and result.stderr is None:
            output_str += "Not output produced \n"
        else:
            output_str +=f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"

        return output_str
        
    except Exception as e:
        return f'Error: executing python file: {e}'