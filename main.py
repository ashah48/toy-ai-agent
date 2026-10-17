import os 
from dotenv import load_dotenv # load the environment variables 
from openai import OpenAI # load the OpenAI class from the openai API
import argparse # Now we can handle command-line arguments
import json
from config import available_functions, system_prompt, working_directory, MAX_ITERATIONS
from functions.call_function import call_function

def create_chat(messages: list):
    # Read the OpenRouter API key
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("OpenRouter environment variable not found.")

    # Point the openai client's base_url to OpenRouter
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)   
    
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )  

    return response

def main(): 
    msg_chain = [
        {"role": "system", "content": system_prompt},
    ]
    # Initialize parser object, add next user prompt to msg_chain
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    msg_chain.append({"role": "user", "content": args.user_prompt})
    
    for _ in range(MAX_ITERATIONS):
        # Get the model's response object
        response = create_chat(msg_chain)

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            # Print number of tokens consumed by prompt & response
            prompt_tokens = response.usage.prompt_tokens
            print(f"Prompt tokens: {prompt_tokens}")
            completion_tokens = response.usage.completion_tokens
            print(f"Response tokens: {completion_tokens}")

        msg = response.choices[0].message
        msg_chain.append(msg)
        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                result_message = call_function(tool_call, working_directory, 
                verbose=args.verbose)
                if result_message['content'] is None:
                    raise Exception("Content of a tool call result should be non-empty")
                if args.verbose:
                    print(f"-> {result_message['content']}")
                # Append tool message to the list
                msg_chain.append(result_message)
        else:
            print(msg.content)
            return 0

    # No final output reached after max iterations
    return 1

if __name__ == "__main__":
    main()
