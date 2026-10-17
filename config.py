# Max number of iterations of API calls
MAX_ITERATIONS = 20

# Max file read output
MAX_CHARS = 10000

# working directory
working_directory = "./calculator"

# system prompt
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

When the user asks to run or execute a Python file, use run_python_file directly. Do not list files first unless the user asks for a listing or the requested file path is unclear. If the user explicitly names a tool, use that tool rather than substituting another.

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# available function descriptions for the model to use as tools
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the contents of a file at a path relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a python file with optional arguments at a file path relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional command-line arguments to pass to the Python file"
                },
            },
            "required": ["file_path"],
        },
    },
}

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes/overwrites to a file at a path relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "What is written onto the file at file_path"
                },
            },
            "required": ["file_path", "content"]
        },
    },
}

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file
]


