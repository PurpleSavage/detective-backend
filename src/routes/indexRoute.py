from flask import Blueprint
from flask import  request, jsonify
from ..controllers import generate_response_ai


index_blueprient= Blueprint('index_blueprint',__name__)
@index_blueprient.route('/scraper', methods=['POST'])
def index():
    data = request.json  # Asumiendo que envías los datos como JSON
    url = data.get('targetUrl')

    if not url:
        return jsonify({'error': 'No se proporcionó URL'}), 400
    
    try:
        data=generate_response_ai(url)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500