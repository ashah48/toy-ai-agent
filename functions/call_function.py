# functions/call_function.py
import json
from collections.abc import Callable

# Import our functions
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

# Define a function mapping from name to actual function
function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file
}

def call_function(tool_call, working_directory: str, 
    verbose: bool = False) -> dict:
    # Get the name of the function and the args
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    
    if function_name in function_map:
        function_args["working_directory"] = working_directory
        result = function_map[function_name](**function_args)
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"{result}",
        }

    else:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }
    

    
