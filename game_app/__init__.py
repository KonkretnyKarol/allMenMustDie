from flask import Flask
import os
from .extensions import db, bcrypt, login_manager, scheduler
from .scheduler import init_scheduler

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')
    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    # Import and register blueprints
    from game_app.routes import main_bp
    app.register_blueprint(main_bp)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        from .models import Village
        db.create_all()
        init_scheduler(app)
    
    return app
