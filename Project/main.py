from fastapi import FastAPI
from groq import Groq

app = FastAPI()

# Put your API key here
client = Groq(api_key="YOUR_API_KEY")

@app.get("/")
def home():
    return {"message": "Server is running"}

@app.post("/chat")
def chat(user_message: str):
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    
    reply = response.choices[0].message.content
    
    return {"reply": reply}