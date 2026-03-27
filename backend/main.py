from fastapi import FastAPI
from data import farming_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to ShambaSmart 🌱"}

@app.get("/ask")
def ask(question: str):
    question = question.lower()

    # Crop logic
    if "maize" in question:
        if "plant" in question or "grow" in question:
            return {"answer": farming_data["maize"]["planting"]}
        elif "fertilizer" in question:
            return {"answer": farming_data["maize"]["fertilizer"]}
        else:
            return {"answer": "Maize is a staple crop widely grown in Africa."}

    # Poultry logic
    elif "chicken" in question or "poultry" in question:
        if "feed" in question:
            return {"answer": farming_data["poultry"]["feeding"]}
        elif "egg" in question:
            return {"answer": farming_data["poultry"]["eggs"]}
        else:
            return {"answer": "Poultry farming is a profitable agricultural activity."}

    return {"answer": "Sorry, I am still learning. Try asking about maize or poultry."}