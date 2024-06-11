# streaming-07-final
* Author: Prabha Sapkota
* Date: 06/11/2024

## Objective: 
To create a project where a producer and consumer are connected via RabbitMQ, by generating simulated inventory updates (including new items added, items removed, and item quantities updated) using the Faker library to generate fake dataset.The aim is to explore the effectiveness and feasibility of the RabbitMQ messaging system in handling real-time inventory management with synthetic data.

## Task 1: Create a place to work
* In GitHub, create a new repo for your project - name it * *
* Add a README.md during the creation process. (If not, you can always add it later.)
* Clone your repo down to your machine.
* In VS Code,add a .gitignore (use one from an earlier module), start working on the README.md Create it if you didn't earlier.
* Create a virtual working environment (.venv) and activate it. 
* Install faker and pika libarary in your active working environment.
* Active RabbitMQ service is required.

## Task 2: Design and implement to generate fake data using faker
* Write python script to generate fake inventoery datasets using faker.
* Name the csv files as "inventory_updates.csv"
* Run the python script to generate data saved to inventory_updates.csv

## Task 3: Design and Implement Your producer
* Design producer.py
* Use the logic, approach, and structure from Module 4, version 2 and version 3.
* These provide a current and solid foundation for streaming analytics - modifying them to serve your purpose IS part of the assignment.
* Do not start from scratch - do not search for code - do not use a notebook.
* Use comments in the code and repo to explain your work.
* Document your project works - display screenshots of your console and maybe the RabbitMQ console.

## Task 4: Design and Implement your consumer
* Design consumer.py
* Use the logic, approach, and structure from prior modules (use the recommended versions)Modifying them to serve your purpose IS part of the assignment.
* Do not start from scratch - do not search for code - do not use a notebook.
* Use comments in the code and repo to explain your work.
* Use docstring comments and add your name and date to your README and your code files.

## Execute the python script
* In Vscode open termional and split it to make two working terminals.
* Run producer.py in one console. This will begin sending messages to RabbitMQ.
* In another console, run consumer.py. This will receive and process messages from RabbitMQ

## Add Email alerts (optional)
* Configure.env.toml with appropriate email configuration settings
   * outgoing_email_host = "smtp.example.com"
   * outgoing_email_port = XXX
   * outgoing_email_address = "your_email@example.com"
   * outgoing_email_password = "your_password"

 ## Screenshots
 ![Alt text](<image showing two working terminals.png>)
 ![Alt text](<email alerts.png>)
 ![Alt text](<datasets generated using faker.png>)









   
