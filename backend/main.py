from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome to ShambaSmart!"}

@app.get("/ask")
def ask(question: str):
    return {
        "question": question,
        "answer": "This is a placeholder response. AI coming soon!"
    }