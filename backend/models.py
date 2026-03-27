from sqlalchemy import Column, Integer, String
from database import Base

class FarmingTip(Base):
    __tablename__ = "farming_tips"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    topic = Column(String)
    content = Column(String)