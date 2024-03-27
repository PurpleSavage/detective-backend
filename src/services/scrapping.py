import requests
from bs4 import BeautifulSoup
import json
class ScraperBot():
    config = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    def __init__(self,target_url):
        self.target_url=target_url
        self.tree=self.request_and_response()
        
        
    def request_and_response(self):
       result = requests.get(self.target_url,headers=self.config)
       return result.text
   
    def extract_data(self):
        soup=BeautifulSoup(self.tree,'lxml')
        data={
            'h1': [h1.get_text(strip=True) for h1 in soup.find_all('h1')],
            'h2': [h2.get_text(strip=True) for h2 in soup.find_all('h2')],
            'h3': [h3.get_text(strip=True) for h3 in soup.find_all('h3')],
            'h4': [h4.get_text(strip=True) for h4 in soup.find_all('h4')],
            'content':[p.get_text(strip=True) for p in soup.find_all('p')],
            'metadata' :{
                'language': soup.html.get('lang', ''),
                'title': soup.title.string if soup.title else ''
            }
        }
        return data