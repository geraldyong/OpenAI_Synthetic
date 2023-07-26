# OpenAI_Synthetic

This repository contains a script that will read a prompt from a text file and send it to OpenAI's API. The code is adapted from one of OpenAI's examples https://platform.openai.com/examples/default-spreadsheet-gen (subject to the MIT License).

There is a Python version and a Bash version. Both of these scripts can be used on its own and achieves the same result.

## Prerequisites

* You will need to have an OpenAI API account, with available usage tokens.
* You will also need an API Key, which you can create from https://platform.openai.com/account/api-keys
  Save the key in the folder that you have pulled this repository to, into a file.
* You will need Python3 with the following libraries installed: `openai`, `base64`

## Steps

1. Edit `openai_submit.py` or `openai_submit.sh` to put in the name of the file in which you have stored your API key.
2. Create prompt files as required. You can use the prompt files provided here `prompt_xxxx.txt` as examples.
3. Run the script and pass in the name of the prompt file:
   e.g. for Python script: `./openai_submit.py prompt_Synthetic.txt`
   e.g. for Bash script: `./openai_submit.sh prompt_Synthetic.txt`
