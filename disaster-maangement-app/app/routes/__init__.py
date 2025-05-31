from flask import Blueprint

from .auth import auth_bp

# from .admin import admin_bp
# from .public import public_bp
from .home import home_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    
  