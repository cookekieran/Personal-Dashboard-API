import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import smtplib
from email.message import EmailMessage

load_dotenv()

EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_ADDRESS2 = os.getenv("EMAIL_ADDRESS2")

server = "http://127.0.0.1:5000/"

response = requests.get(server + "/")

def get_news():
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

    return news_list


def send_email(news_list):
    msg = EmailMessage()
    msg["Subject"] = "Daily News"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS2

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

    print("email sent successfully")

# uncomment to send email
news = get_news()
send_email(news)

