from database import SessionLocal
from models import FarmingTip

db = SessionLocal()

tips = [
    FarmingTip(category="maize", topic="planting", content="Plant maize at the start of rains."),
    FarmingTip(category="maize", topic="fertilizer", content="Use DAP during planting."),
    FarmingTip(category="poultry", topic="feeding", content="Feed broilers starter and grower feeds."),
]

for tip in tips:
    db.add(tip)

db.commit()
db.close()

print("Database initialized!")