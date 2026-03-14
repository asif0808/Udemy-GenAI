from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
SYSTEM_PROMPT='''You are a coding expert and your name is Guido
Example: 
Q. Write code for adding two numbers
A. Sure , Myself Guido and here is your python code for adding two numbers
def sum(a,b):
    return a+b'''
client=OpenAI(api_key=os.getenv("GEMINI_API_KEY"),
              base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Write code for substracting two numbers"}

    ]
)
print(response.choices[0].message.content)
