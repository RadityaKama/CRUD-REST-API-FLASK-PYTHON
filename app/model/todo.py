from app import db
from datetime import datetime
from app.model.user import Users

class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Todo {}>'.format(self.title) 