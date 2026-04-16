from prompts import CODE_GENERATION_PROMPT, TEST_GENERATION_PROMPT
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os, re, json, sys

load_dotenv(Path.cwd() / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Could not find your OpenAI API key! Please add an .env file or set the environment variable OPENAI_API_KEY.")
    sys.exit(1)

#OpenAI Client creation
def try_get_client(key : str) -> OpenAI:
    try:
        client = OpenAI(api_key= key)
        return client
    except Exception as e:
        raise Exception("Failed to create OpenAI client") from e
    
client = try_get_client(api_key)

#Code generation
def generate_code(description: str) -> str:
    
    messages = [
        {"role": "user", "content": CODE_GENERATION_PROMPT.format(description= description)}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.2
    )

    code = clean_code_output(response.choices[0].message.content)

    test_messages = [
        {"role": "user", "content": TEST_GENERATION_PROMPT.format(code= code)}
    ]

    test_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=test_messages,
        temperature=0.2
    )

    tests = clean_code_output(test_response.choices[0].message.content)

    return code, tests

#Output cleaning 
def clean_code_output(response : str) -> str:
    match = re.search(r"```(?:python)?\s*(.*?)```", response, re.DOTALL)
    if match:
        return match.group(1).strip()

    return response.strip()

#Save code to file
def save_code(code: str, filename: str):

    if not filename.endswith(".py"):
        filename = f"{filename}.py"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Code saved to {os.path.abspath(filename)}")


