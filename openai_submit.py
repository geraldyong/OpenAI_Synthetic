#!/opt/homebrew/bin/python3

# This code contains code snippets from OpenAI examples which are subject to MIT License.
# Please refer to the LICENSE file for more details.
#
# This code is from https://github.com/geraldyong/OpenAI_Synthetic
# Written by Gerald Yong
# July 2023
#
# Versions
# 1.0 - July 2023 - First Release
# 2.0 - Jan 2024 - Updated for OpenAI library

# Import required libraries.
import sys
import base64
from openai import OpenAI
from pathlib import Path

# Check for the file passed in.
if len(sys.argv) > 1:
    prompt_file = sys.argv[1]
else:
    print("Please provide a text file containing the prompt.")
    print("Usage: " + sys.argv[0] + " <prompt_file>")
    exit()

# Read the base64 encoded API Key and decode it. 
api_key = base64.b64decode(Path('GeraldYong_APIKey_encoded.txt').read_text().rstrip())
client = OpenAI(
  api_key = api_key.decode('ascii').rstrip()
)

# Read the Prompt Text into a variable.
prompt_text = Path(prompt_file).read_text()

# Sends the prompt to OpenAI by embedding the prompt text.
completion = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  temperature = 0.5,
  max_tokens = 300,
  messages = [
    {"role": "system", "content": prompt_text},
  ]
)

# Prints out the response from OpenAI.
print(completion.choices[0].message.content)
