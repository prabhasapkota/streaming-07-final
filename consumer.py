import pika
import json
import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values

# Load email configuration from .env.toml file
secret_dict = dotenv_values('.env.toml')
smtp_server = secret_dict["outgoing_email_host"]
smtp_port = int(secret_dict["outgoing_email_port"])
smtp_user = secret_dict["outgoing_email_address"]
smtp_password = secret_dict["outgoing_email_password"]

# Function to send email alert
def send_email(subject, body):
    msg = EmailMessage()
    msg['From'] = smtp_user
    msg['To'] = smtp_user  # Sending email to yourself for testing, change it to recipient_email if needed
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        print('Email sent successfully')
    except Exception as e:
        print('Failed to send email:', str(e))

# Define callback function for consuming messages
def callback(ch, method, properties, body):
    update = json.loads(body.decode())
    print("Received:", update)
    subject = "Inventory Update Notification"
    email_body = ""

    # Process the inventory update based on its action
    if update['action'] == 'added':
        email_body = f"New item added: {update['item_name']} - Quantity: {update['quantity']}"
        print("New item added:", update['item_name'], "- Quantity:", update['quantity'])
    elif update['action'] == 'removed':
        email_body = f"Item removed: {update['item_name']} - Quantity: {update['quantity']}"
        print("Item removed:", update['item_name'], "- Quantity:", update['quantity'])
    elif update['action'] == 'updated':
        email_body = f"Item updated: {update['item_name']} - New Quantity: {update['quantity']}"
        print("Item updated:", update['item_name'], "- New Quantity:", update['quantity'])

    # Send email alert
    send_email(subject, email_body)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='inventory_updates')

# Consume messages from the queue
channel.basic_consume(queue='inventory_updates',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for inventory updates. To exit press CTRL+C')
channel.start_consuming()
