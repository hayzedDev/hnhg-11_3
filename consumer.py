import pika
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

rabbitmq_host = 'localhost'
queue_name = 'email_queue'

def send_email(to_email):
    smtp_server = os.getenv('BREVO_SMTP_SERVER')
    smtp_port = int(os.getenv('BREVO_SMTP_PORT'))
    smtp_user = os.getenv('BREVO_SMTP_USER')
    smtp_password = os.getenv('BREVO_SMTP_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = 'Testing Shege'

    body = "Welcome to HNG. If you're seeing this, it means @HayzedDev is done with his task"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(smtp_user, to_email, text)
    server.quit()

def callback(ch, method, properties, body):
    message = json.loads(body)
    if message['action'] == 'send_email':
        to_email = message['to_email']
        send_email(to_email)
    ch.basic_ack(delivery_tag=method.delivery_tag)

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
except pika.exceptions.AMQPConnectionError as e:
    print(f"Error connecting to RabbitMQ: {e}")
except Exception as e:
    print(f"An error occurred: {e}")