# OpenAI_Synthetic

This repository contains a Python script that will read a prompt from a text file and send it to OpenAI.

## Prerequisies

* You will need to have an OpenAI API account, with available usage tokens.
* You will also need an API Key, which you can create from https://platform.openai.com/account/api-keys
  Save the key in the folder that you have pulled this repository to, into a file.
* You will need Python3 with the following libraries installed: `openai`

## Steps

1. Edit `openai_demo.py` to put in the name of the file in which you have stored your API key.
2. Create prompt files as required. You can use the prompt files provided as a sample.
3. Run the script and pass in the name of the prompt file:
   `./openai_demo.py prompt.txt` 