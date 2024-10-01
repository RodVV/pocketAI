from flask import Blueprint, request, jsonify
from .services.example_service import get_all_items, create_new_item, update_item, delete_item
from .crawler.run_spider import run_spider

main_bp = Blueprint('main', __name__)

data_store = {}


@main_bp.route('/get', methods=['GET'])
def get_response():
    user_message = request.args.get('message')  # Obtém a mensagem do usuário
    # Processa a mensagem e gera uma resposta
    response_message = f"Você disse: {user_message}"  # Exemplo de resposta
    return jsonify({"userMessage": response_message})


@main_bp.route('/crawl', methods=['GET'])
def crawl():
    search_term = request.args.get('search_term')  # Recebe o termo de busca do front-end
    if not search_term:
        return jsonify({'error': 'Search term is required'}), 400

    # Executa o spider do Scrapy e coleta os resultados
    results = run_spider(search_term)

    return jsonify(results)

# @main_bp.route('/items', methods=['POST'])
# def create_item():
#     data = request.get_json()
#     new_id = create_new_item(data_store, data['name'], data['description'])
#     return jsonify({'message': 'Item created successfully', 'id': new_id}), 201


# @main_bp.route('/items/<int:item_id>', methods=['PUT'])
# def update_item_route(item_id):
#     data = request.get_json()
#     if not update_item(data_store, item_id, data['name'], data['description']):
#         return jsonify({'message': 'Item not found'}), 404
#     return jsonify({'message': 'Item updated successfully'})

# @main_bp.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item_route(item_id):
#     if not delete_item(data_store, item_id):
#         return jsonify({'message': 'Item not found'}), 404
#     return jsonify({'message': 'Item deleted successfully'})
