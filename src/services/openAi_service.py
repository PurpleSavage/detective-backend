from openai import OpenAI
from decouple import config
from ..definiitions_personalitys import PERSONALITY_GENERATE_ANALIST

class Inspector():
    def __init__(self,estructure_html):
        self.estructure_html=estructure_html
        
    def generate_response(self):
        client = OpenAI(api_key=config('SECRET_KEY'))
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role":"system", 
                    "content":PERSONALITY_GENERATE_ANALIST
                },
                {
                    "role":"user",
                    "content":self.estructure_html
                }
            ]
        )

        bot_response= response.choices[0].message.content
        
        return bot_response
