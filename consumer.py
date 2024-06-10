import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='inventory_updates')

# Define callback function for consuming messages
def callback(ch, method, properties, body):
    update = json.loads(body.decode())
    print("Received:", update)
    # Process the inventory update based on its action
    if update['action'] == 'added':
        print("New item added:", update['item_name'], "- Quantity:", update['quantity'])
        # Process new item added
    elif update['action'] == 'removed':
        print("Item removed:", update['item_name'], "- Quantity:", update['quantity'])
        # Process item removed
    elif update['action'] == 'updated':
        print("Item updated:", update['item_name'], "- New Quantity:", update['quantity'])
        # Process item quantity updated

# Consume messages from the queue
channel.basic_consume(queue='inventory_updates',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for inventory updates. To exit press CTRL+C')
channel.start_consuming()
