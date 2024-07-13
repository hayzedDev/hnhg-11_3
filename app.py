# app.py
from fastapi import FastAPI, Request
import pika
import aiofiles
import time
import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# RabbitMQ connection parameters
rabbitmq_host = 'localhost'
queue_name = 'email_queue'

def send_to_rabbitmq(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    connection.close()

# def send_email(to_email):
#     smtp_server = os.getenv('BREVO_SMTP_SERVER')
#     smtp_port = os.getenv('BREVO_SMTP_PORT')
#     smtp_user = os.getenv('BREVO_SMTP_USER')
#     smtp_password = os.getenv('BREVO_SMTP_PASSWORD')

#     msg = MIMEMultipart()
#     msg['From'] = smtp_user
#     msg['To'] = to_email
#     msg['Subject'] = 'Test Email'

#     body = 'This is a test email sent from FastAPI application.'
#     msg.attach(MIMEText(body, 'plain'))

#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
#     server.login(smtp_user, smtp_password)
#     text = msg.as_string()
#     server.sendmail(smtp_user, to_email, text)
#     server.quit()

@app.get("/")
async def main(request: Request):
    query_params = request.query_params

    if 'sendmail' in query_params:
        to_email = query_params['sendmail']
        message = {"action": "send_email", "to_email": to_email}
        send_to_rabbitmq(message)
        return {"status": "Email task queued"}

    if 'talktome' in query_params:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        async with aiofiles.open('/var/log/messaging_system.log', mode='a') as f:
            await f.write(f"{current_time}\n")
        return {"status": "Time logged"}

    return {"status": "No valid query parameter provided"}