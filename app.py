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
FRED_API_KEY = os.getenv("FRED_API_KEY")

if not NEWS_API_KEY:
    raise RuntimeError("NEWS_API_KEY is not set")

if not FRED_API_KEY:
    raise RuntimeError("FRED_API_KEY is not set")

print("API KEYS loaded successfully")


NEWS_BASE = "https://newsapi.org/v2"
FRED_BASE = "https://api.stlouisfed.org"

START_DATE = "2010-01-01"


SERIES = {
    "fed_funds": "EFFR",
    "2y": "DGS2",
    "10y": "DGS10",
    "10y_2y_spread": "T10Y2Y",
    "fed_assets": "WALCL",
    "bank_reserves": "WRESBAL",
    "core_pce": "PCEPILFE",
    "payrolls": "PAYEMS",
    "unemployment": "UNRATE",
    "real_gdp": "GDPC1",
    "financial_conditions": "NFCI",
}

# HELPER FUNCTION

def get_news(category="business"):
    url = f"{NEWS_BASE}/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return f"error, {response.status_code}"
    return response.json()

def get_fred(series_id):
    url = f"{FRED_BASE}/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json&observation_start={START_DATE}"
    response = requests.get(url)
    if response.status_code != 200:
        return f"error, {response.status_code}"
    return response.json()


class DailyBriefing(Resource):
    def get(self):
        news = get_news()

        macro = {
            name: get_fred(ser)
            for name, ser in SERIES.items()
        }

        time = str(datetime.now())

        return {
            "user": "Kieran",
            "date": time[:10],
            "time": time[11:19],
            "news": news,
            "macro": macro
        }
    
api.add_resource(DailyBriefing, "/")
    
if __name__ == "__main__":
    app.run(debug=True)

