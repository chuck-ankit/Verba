from fastapi import FastAPI
from pydantic import BaseModel
from app.model import generate_response

app = FastAPI()

class MessageInput(BaseModel):
    instruction: str
    input_text: str

@app.post("/chat/")
async def chat(message: MessageInput):
    response = generate_response(message.instruction, message.input_text)
    return {"response": response}
