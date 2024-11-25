from flask import Flask
from config import Config
from db import db, init_db
from app.routes.user_routes import user_routes
from app.routes.order_routes import order_routes
from app.routes.shipment_routes import shipment_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    init_db(app)

    # Register blueprints
    app.register_blueprint(user_routes, url_prefix='/api')
    app.register_blueprint(order_routes, url_prefix='/api')
    app.register_blueprint(shipment_routes, url_prefix='/api')

    return app
