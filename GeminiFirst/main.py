from google import genai
client=genai.Client(
    api_key='AIzaSyAtNCJ_WndNEoeqagMtqK1oHiU5N7oIFds'
)
response=client.models.generate_content(
    model='gemini-2.5-flash',contents='Explain how ai works in fewer words'
)
print(response.text)