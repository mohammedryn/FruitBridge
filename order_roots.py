from flask import Blueprint, jsonify, request
from models.order_model import Order
from db import db

order_routes = Blueprint('order_routes', __name__)

@order_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    description = data.get('description')

    # Input validation
    if not user_id or not description:
        return jsonify({"error": "User  ID and description are required"}), 400

    # Additional validation can be added here (e.g., type checking)

    new_order = Order(user_id=user_id, description=description)

    try:
        db.session.add(new_order)
        db.session.commit()
        return jsonify({
            "message": "Order created successfully",
            "order": {
                "id": new_order.id,  # Assuming the Order model has an 'id' attribute
                "user_id": new_order.user_id,
                "description": new_order.description
            }
        }), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": str(e)}), 500  # Return error message