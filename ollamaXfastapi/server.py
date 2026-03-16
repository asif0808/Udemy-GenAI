from fastapi import FastAPI,Body
from ollama import Client
app = FastAPI()
client=Client(
    host="http://localhost:11434"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
@app.get("/contact-us")
def read_item():
    return {"email":"aasif911496@gmail.com"}
@app.post("/chat")
def chat(
        message: str=Body(..., description="The message")
):
    response=client.chat(model="gemma2:2b",messages=[
        {"role":"user","content":message}
    ])
    return {"response":response.message.content}
