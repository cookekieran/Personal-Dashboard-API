import requests
from functions import get_news, get_fred
from email_script import send_email



server = "http://127.0.0.1:5000/"

response = requests.get(server + "/")

raw_json = response.json()

news = get_news(raw_json)
macro_df = get_fred(raw_json)

send_email(news)