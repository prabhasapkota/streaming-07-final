import csv
import random
from datetime import datetime, timedelta
from faker import Faker



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

def save_inventory_updates_to_csv(num_updates, filename):
    '''Generates random inventory updates and saves them to a CSV file.'''
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['item_name', 'action', 'quantity', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for _ in range(num_updates):
            update = generate_random_inventory_update()
            writer.writerow(update)

# Generate and save 100 random inventory updates to a CSV file named 'inventory_updates.csv'
save_inventory_updates_to_csv(100, 'inventory_updates.csv')


