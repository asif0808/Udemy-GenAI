# Chain OF Thought Prompting
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
SYSTEM_PROMPT='''You are a coding expert in python while giving the response explain each and evey step from initialization to execution (chain of thought) before giving final  answer'''
client=OpenAI(api_key=os.getenv("GEMINI_API_KEY"),
              base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"write a program to store and print int values"}
    ]
)
print(response.choices[0].message.content)