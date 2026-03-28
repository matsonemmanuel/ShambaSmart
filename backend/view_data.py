from database import SessionLocal
from models import FarmingTip

db = SessionLocal()

tips = db.query(FarmingTip).all()

for tip in tips:
    print(f"{tip.id} | {tip.category} | {tip.topic} | {tip.content}")

db.close()