from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
SYSTEM_PROMPT='''You are expert in coding and answer only coding related questions
Example:
    Q.write a program to add three numbers
    A. This is a programming question not theoretical ,Hence heres the program
    def Sum(a,b,c):
        return a+b+c
    Q.what is mutable and immutable type in python?
    A.this is not a programming question hence here is the theoretical answer
    string,int,tuple are immutable where as list,dict,set and dict are mutable
    Q.what is the day today?
    A. Sorry for inconvenience, I can answer only coding related questions'''
client=OpenAI(api_key=os.getenv("GEMINI_API_KEY"),
              base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        # {"role":"user","content":"What is the color of sky?"}
        #  {"role":"user","content":"What is the use of pass statement?"}
        # {"role":"user","content":"What is method overloading?"}
                # {"role":"user","content":"What is method overriding?"}
        # Structured output using few shot prompting
     {"role":"user","content":"Write program to multiply three number, output format : Sure here is the code in json format {{}}?"}
    ]
)
print(response.choices[0].message.content)