import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import smtplib
from email.message import EmailMessage

load_dotenv()

EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

server = "http://127.0.0.1:5000/"

response = requests.get(server + "/")

if response.status_code == 200:
    news_list = []
    data = response.json()
    articles = data['news']['articles']

    for article in articles:
        news_dict = {
            "source": article['source']['name'],
            "author": article['author'],
            "url": article['url'],
            "title": article['title'],
            "publish time": datetime.fromisoformat(article['publishedAt'])
        }
        news_list.append(news_dict)
    
    # sort by date published (newest first)
    news_list.sort(key=lambda x: x["publish time"], reverse=True)

else:
    print("Error:", response.status_code)


def send_email():
    msg = EmailMessage()
    msg["Subject"] = "Daily News"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    email_contents = "Here are the most reent news stories:\n"
    for i, article in enumerate(news_list):
        source = article["source"]
        title = article['title']
        url = article['url']
        publish_time = article['publish time'].strftime("%d %b %Y %H:%M")
        email_contents += f"{i}. {source} -  {title} ({publish_time})\n{url}\n\n"
    
    msg.set_content(email_contents)
    

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        smtp.send_message(msg)

    print("Email sent successfully!")

send_email()