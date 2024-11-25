from flask import Blueprint, jsonify, request
from models.shipment_model import Shipment
from db import db

shipment_routes = Blueprint('shipment_routes', __name__)

@shipment_routes.route('/shipments', methods=['POST'])
def create_shipment():
    data = request.get_json()
    order_id = data.get('order_id')
    carrier = data.get('carrier')
    if not order_id or not carrier:
        return jsonify({"error": "Order ID and carrier are required"}), 400

    new_shipment = Shipment(order_id=order_id, carrier=carrier)
    db.session.add(new_shipment)
    db.session.commit()
    return jsonify({"message": "Shipment created successfully"}), 201
