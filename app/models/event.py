from app import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)

    participants = db.relationship('User', backref='event', lazy=True) 

    def __repr__(self):
        return f"<Event {self.name}>"
