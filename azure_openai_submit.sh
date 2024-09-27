#!/bin/bash

# This code contains code snippets from OpenAI examples which are subject to MIT License.
# Please refer to the LICENSE file for more details.
#
# This code is from https://github.com/geraldyong/OpenAI_Synthetic
# Written by Gerald Yong
# July 2023
#
# Versions
# 1.0 - Jan 2024 - First release for Azure OpenAI

# Obtain command line arguments.
prompt_file=$1

# Check for the file passed in.
if [ "${prompt_file}" = "" ]; then
  echo "Please provide a text file containing the prompt."
  echo "Usage: ${0} <prompt_file>"
  exit
fi

# Read the OPENAI parameters from the environment.
api_base=${OPENAI_API_BASE}
api_version=${OPENAI_API_VERSION}
api_endpoint=${api_base}/deployments/${OPENAI_API_DEPLOYMENT}/completions?api-version=${api_version}
api_key=${OPENAI_API_KEY}

# Read the Prompt Text into a variable.
prompt_text=`cat ${prompt_file} | awk '{printf "%s\\\n", $0}'`

# Sends the prompt to OpenAI by embedding the prompt text in a curl command.
response=`echo curl -sk ${api_endpoint} \
  -H \"Content-Type: application/json\" \
  -H \"api-key: ${api_key}\" \
  -d "'{
      \"prompt\": \"${prompt_text}\",
      \"temperature\": 0.5,
      \"max_tokens\": 300
  }'" \
| sh | egrep "\"text\":" | sed 's/.*"text"://' | sed -e 's/^"//' -e 's/"$//'`

# Prints out the response from OpenAI.
echo -e ${response}
