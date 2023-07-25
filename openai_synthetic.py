#!/opt/homebrew/bin/python3

# Import required libraries.
import sys
import openai
from pathlib import Path

# Check for the file passed in.
if len(sys.argv) > 1:
    prompt_file = sys.argv[1]
else:
    print("Please provide a text file containing the prompt.")
    print("Usage: " + sys.argv[0] + " <prompt_file>")
    exit()

# Read the API Key and Prompt Text.
openai.api_key = Path('/Users/geraldyong/GitHub/ChatGPT/GeraldYong_APIKey_Google.txt').read_text().rstrip()
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
