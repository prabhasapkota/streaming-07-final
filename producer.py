import pika
import json
import random
from datetime import datetime
from faker import Faker
from time import sleep

# Initialize the Faker library
fake = Faker()

# Define lists of random attributes for inventory items
item_names = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E']
actions = ['added', 'removed', 'updated']

def generate_random_inventory_update():
    '''Generates and returns a random inventory update.'''
    item_name = random.choice(item_names)
    action = random.choice(actions)
    quantity = random.randint(1, 100)  # Random quantity between 1 and 100
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    update = {
        'item_name': item_name,
        'action': action,
        'quantity': quantity,
        'timestamp': timestamp
    }
    return update

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='inventory_updates')

# Publish fake inventory updates to RabbitMQ
while True:
    fake_update = generate_random_inventory_update()
    channel.basic_publish(exchange='',
                          routing_key='inventory_updates',
                          body=json.dumps(fake_update))
    print("Sent:", fake_update)
    sleep(1)  # Simulate updates every second

connection.close()