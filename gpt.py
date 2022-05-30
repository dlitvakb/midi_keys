import os
import pyperclip
import openai

OPEN_AI_ORG = os.getenv("OPEN_AI_ORG")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
GPT_MODEL = "gpt-3.5-turbo-16k"

openai.organization = OPEN_AI_ORG
openai.api_key = OPEN_AI_KEY


def summarise_gpt(name, _attributes, quiet):
    to_summarise = pyperclip.paste()
    gpt_prompt = [
        {
            "role": "system",
            "content": "Create a summary of the provided text, keep tone of voice and language",
        },
        {"role": "user", "content": to_summarise},
    ]
    completion = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=gpt_prompt,
        temperature=0.5,
        n=1,
    )
    response = completion["choices"][0]["message"]["content"]
    if not quiet:
        print(name, "-", response)
    pyperclip.copy(response)
