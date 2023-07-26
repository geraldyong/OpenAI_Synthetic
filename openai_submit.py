#!/opt/homebrew/bin/python3

# Import required libraries.
import sys
import openai
import base64
from pathlib import Path

# Check for the file passed in.
if len(sys.argv) > 1:
    prompt_file = sys.argv[1]
else:
    print("Please provide a text file containing the prompt.")
    print("Usage: " + sys.argv[0] + " <prompt_file>")
    exit()

# Read the base64 encoded API Key and decode it. 
# Read the Prompt Text into a variable.
api_key = base64.b64decode(Path('GeraldYong_APIKey_Google_encoded.txt').read_text().rstrip())
openai.api_key = api_key.decode('ascii').rstrip()
prompt_text = Path(prompt_file).read_text()

# Sends the query to ChatGPT by embedding the prompt text.
completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 1,
  max_tokens = 300,
  messages = [
    {"role": "system", "content": prompt_text},
  ]
)

# Prints out the response from ChatGPT.
print(completion.choices[0].message["content"])