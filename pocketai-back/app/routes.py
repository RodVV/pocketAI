from flask import Blueprint, request, jsonify
from .services.example_service import get_all_items, create_new_item, update_item, delete_item

main_bp = Blueprint('main', __name__)

data_store = {}

@main_bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_id = create_new_item(data_store, data['name'], data['description'])
    return jsonify({'message': 'Item created successfully', 'id': new_id}), 201

@main_bp.route('/items', methods=['GET'])
def get_items():
    return jsonify(get_all_items(data_store))

@main_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item_route(item_id):
    data = request.get_json()
    if not update_item(data_store, item_id, data['name'], data['description']):
        return jsonify({'message': 'Item not found'}), 404
    return jsonify({'message': 'Item updated successfully'})

@main_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item_route(item_id):
    if not delete_item(data_store, item_id):
        return jsonify({'message': 'Item not found'}), 404
    return jsonify({'message': 'Item deleted successfully'})
