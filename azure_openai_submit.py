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
import os
import sys
from openai import AzureOpenAI
from pathlib import Path

# Check for the file passed in.
if len(sys.argv) > 1:
    prompt_file = sys.argv[1]
else:
    print("Please provide a text file containing the prompt.")
    print("Usage: " + sys.argv[0] + " <prompt_file>")
    exit()

# Read the base64 encoded API Key and decode it. 
api_base = os.environ["OPENAI_API_BASE"]
api_key = os.environ["OPENAI_API_KEY"]
api_version = os.environ["OPENAI_API_VERSION"]
api_deployment = os.environ["OPENAI_API_DEPLOYMENT"]
api_endpoint = api_base + "/deployments/" + api_deployment + "/completions?api-version=" + api_version

client = AzureOpenAI(
  api_key = api_key,
  api_version = api_version,
  azure_endpoint = api_endpoint
)

# Read the Prompt Text into a variable.
prompt_text = Path(prompt_file).read_text()

# Sends the prompt to OpenAI by embedding the prompt text.
completion = client.completions.create(
  model = api_deployment,
  temperature = 0.5,
  max_tokens = 300,
  prompt = prompt_text
)

# Prints out the response from OpenAI.
print(completion.choices[0].text)
