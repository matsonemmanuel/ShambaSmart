from fastapi import FastAPI
from database import SessionLocal, engine
from models import Base, FarmingTip

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to ShambaSmart 🌱"}


@app.get("/ask")
def ask(question: str):
    # Open database session
    db = SessionLocal()

    question = question.lower()

    result = None

    # Maize logic
    if "maize" in question:
        if "plant" in question or "grow" in question:
            result = db.query(FarmingTip).filter_by(
                category="maize", topic="planting"
            ).first()

        elif "fertilizer" in question:
            result = db.query(FarmingTip).filter_by(
                category="maize", topic="fertilizer"
            ).first()

    # Poultry logic
    elif "chicken" in question or "poultry" in question:
        if "feed" in question:
            result = db.query(FarmingTip).filter_by(
                category="poultry", topic="feeding"
            ).first()

    # Close database session
    db.close()

    # Return response
    if result:
        return {
            "question": question,
            "answer": result.content
        }
    else:
        return {
            "question": question,
            "answer": "Sorry, I am still learning. Try another question."
        }