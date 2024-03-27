from ..services import Inspector, ScraperBot
import json 
def generate_response_ai(url_target):
    try:
        bot = ScraperBot(url_target)
        data = bot.extract_data()
        inspector = Inspector( json.dumps(data))
        response = inspector.generate_response()
        return {
                    'content':response,
                    'h1':data['h1'],
                    'associated_data':data['metadata']
                }  
    except Exception as e:
        # Aquí puedes hacer logging del error, si es necesario
        print(f"Error en generate_response_ai: {e}")
        raise  # Propagar el error para manejarlo en la capa superior