import os
from dotenv import load_dotenv
import requests
from flask import Flask
from flask_restful import Api, Resource
from datetime import datetime

load_dotenv()

app = Flask(__name__)
api = Api(app)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise RuntimeError("NEWS_API_KEY is not set")

print("API KEY loaded successfully")


NEWS_BASE = "https://newsapi.org/v2"


# HELPER FUNCTION

def get_news(category="business"):
    url = f"{NEWS_BASE}/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return f"error, {response.status_code}"
    return response.json()



class DailyBriefing(Resource):
    def get(self):
        news = get_news()

        time = str(datetime.now())

        return {
            "user": "Kieran",
            "date": time[:10],
            "time": time[11:19],
            "news": news
        }
    
api.add_resource(DailyBriefing, "/")
    
if __name__ == "__main__":
    app.run(debug=True)

