import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path_wdir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wdir, file_path))
    
        # Check if the target file path is
        # within the absolute working directory path
        valid_target_file = os.path.commonpath([abs_path_wdir, target_file]) == abs_path_wdir
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory \n'
    
        # Check if target file is actually a directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Allow new files, but reject an existing path that is not a regular file
        if os.path.exists(target_file) and not os.path.isfile(target_file):
            return f'Error: file not found or is not a regular file "{file_path}"\n'

        # Make sure all the parent directories of the file path exist
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        # Write to file
        with open(target_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'