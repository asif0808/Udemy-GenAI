from openai import OpenAI
from dotenv import load_dotenv
import os
# Zero-Shot Prompting => the model is given direct question or task without any prior example
load_dotenv()
SYSTEM_PROMPT="your name is alexa, you should only and only answer coding related questions and about yourself and say sorry if asked something other than coding"
client=OpenAI(api_key=os.getenv("GEMINI_API_KEY"),
                 base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
              )
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Hello ,Its Aasif, who are u"}
    ]
)
print(response.choices[0].message.content)