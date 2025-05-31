
from app import create_app,db
from app.models import *
import datetime
import os
from app.models.user import User

from datetime import datetime
app=create_app()


DB_PATH = 'community.db'  # or use app.config['SQLALCHEMY_DATABASE_URI'].split:///[-1]



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        user = User.query.filter_by(phone="1234567890").first()
        if not user:
            user = User(
                username="john_doe",
                email="john@example.com",
                phone="1234567890",
                password="test123"
            )
            db.session.add(user)
            db.session.commit()
            print(f"User created: {user}")

        
        app.run(debug=True)