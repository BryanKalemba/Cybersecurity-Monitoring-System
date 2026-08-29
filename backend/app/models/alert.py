from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    rule_name = Column(String, nullable=False)
    severity = Column(String, nullable=False, default="medium")
    status = Column(String, nullable=False, default="open", index=True)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    resolved_at = Column(DateTime(timezone=True), nullable=True)

    device = relationship("Device")
    event = relationship("Event")
    assignee = relationship("User")