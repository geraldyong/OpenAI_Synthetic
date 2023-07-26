#!/bin/bash

# This code contains code snippets from OpenAI examples which are subject to MIT License.
# Please refer to the LICENSE file for more details.
#
# This code is from https://github.com/geraldyong/OpenAI_Synthetic
# Written by Gerald Yong
# July 2023
#
# Versions
# 1.0 - July 2023 - First Release

# Obtain command line arguments.
prompt_file=$1

# Check for the file passed in.
if [ "${prompt_file}" = "" ]; then
  echo "Please provide a text file containing the prompt."
  echo "Usage: ${0} <prompt_file>"
  exit
fi

# Read the base64 encoded API Key and decode it.
# Read the Prompt Text into a variable.
api_key=`cat GeraldYong_APIKey_Google_encoded.txt | base64 --decode`
prompt_text=`cat ${prompt_file} | awk '{printf "%s\\\n", $0}'`

# Sends the prompt to OpenAI by embedding the prompt text in a curl command.
response=`echo curl -sk https://api.openai.com/v1/chat/completions \
  -H \"Content-Type: application/json\" \
  -H \"Authorization: Bearer $api_key\" \
  -d "'{
  \"model\": \"gpt-3.5-turbo\",
  \"messages\": [
    {
      \"role\": \"system\",
      \"content\": \"${prompt_text}\"
    }
  ],
  \"temperature\": 1,
  \"max_tokens\": 300
}'" \
| sh | egrep "\"content\":" | sed 's/.*"content": //' | sed -e 's/^"//' -e 's/"$//'`

# Prints out the response from OpenAI.
echo -e ${response}