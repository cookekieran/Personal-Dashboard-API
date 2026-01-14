import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_ADDRESS2 = os.getenv("EMAIL_ADDRESS2")

def send_email(news_list):
    msg = EmailMessage()
    msg["Subject"] = "Daily News"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS2

    email_contents = "Here are the most recent news stories:\n"
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