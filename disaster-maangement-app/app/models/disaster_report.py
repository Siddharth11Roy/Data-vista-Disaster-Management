from .. import db
from flask_login import UserMixin
class DisasterReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    disaster_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())