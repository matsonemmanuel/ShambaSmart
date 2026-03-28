from fastapi import FastAPI
from database import SessionLocal, engine
from models import Base, FarmingTip
from nlp import predict_intent
from ai import get_ai_response

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to ShambaSmart 🌱 - Smart Farming Assistant"
    }


@app.get("/ask")
def ask(question: str):
    # Open database session
    db = SessionLocal()

    try:
        # Step 1: Predict intent using NLP
        intent = predict_intent(question.lower())

        result = None

        # Step 2: Try to get relevant data from database
        if intent == "maize_planting":
            result = db.query(FarmingTip).filter_by(
                category="maize", topic="planting"
            ).first()

        elif intent == "maize_fertilizer":
            result = db.query(FarmingTip).filter_by(
                category="maize", topic="fertilizer"
            ).first()

        elif intent == "poultry_feeding":
            result = db.query(FarmingTip).filter_by(
                category="poultry", topic="feeding"
            ).first()

        # Step 3: Extract database context (if found)
        db_context = result.content if result else ""

        # Step 4: Get AI-generated response
        ai_answer = get_ai_response(question, db_context)

        # Step 5: Return response
        return {
            "question": question,
            "intent_detected": intent,
            "database_context_used": bool(result),
            "answer": ai_answer
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "Something went wrong. Please try again."
        }

    finally:
        # Always close database session
        db.close()