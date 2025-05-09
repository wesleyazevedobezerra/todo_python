from flask import Flask
from app.models.taskViewModel import init_db
from app.controllers.taskControllers import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    init_db()
    app.register_blueprint(task_bp, url_prefix='/api/task')

    return app