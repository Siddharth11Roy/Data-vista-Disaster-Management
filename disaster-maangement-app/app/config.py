
import os

class Config:
    SECRET_KEY=os.getenv("SECRET_KEY","supersecretkey")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///community.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False