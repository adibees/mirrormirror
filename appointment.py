from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String
import arrow

Base = declarative_base()


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    mood = Column(String(50), nullable=False)
    keyword = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)
    delta = Column(Integer, nullable=False)
    time = Column(DateTime, nullable=False)
    timezone = Column(String(50), nullable=False)

    def __init__(self, mood, keyword, phone_number, delta, time, timezone):
        self.mood = mood
        self.keyword = keyword
        self.phone_number = phone_number
        self.delta = delta
        self.time = time
        self.timezone = timezone

    def __repr__(self):
        return '<Appointment %r>' % self.name

    def get_notification_time(self):
        appointment_time = arrow.get(self.time)
        reminder_time = appointment_time.replace(minutes=-self.delta)
        return reminder_time