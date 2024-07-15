@channel

DevOps Stage 3 Task
Task: Messaging System with RabbitMQ/Celery and Python Application behind Nginx
Objective: Deploy a Python application behind Nginx that interacts with RabbitMQ/Celery for email sending and logging functionality.
Requirements:
Local Setup:
Install RabbitMQ and Celery on your local machine.
Set up a Python application with the following functionalities:
An endpoint that can accept two parameters: ?sendmail and ?talktome.
Endpoint Functionalities:
?sendmail: When this parameter is passed, the system should:
Send an email using SMTP to the value provided (e.g., ?sendmail=destiny@destinedcodes.com).
Use RabbitMQ/Celery to queue the email sending task.
Ensure the email-sending script retrieves and executes tasks from the queue.
?talktome: When this parameter is passed, the system should:
Log the current time to /var/log/messaging_system.log.
Nginx Configuration:
Configure Nginx to serve your Python application.
Ensure proper routing of requests to the application.
Endpoint Access:
Use ngrok or a similar tool to expose your local application endpoint for external access.
Provide a stable endpoint for testing purposes.
Documentation and Walk-through:
Record a screen-captured walk-through of the entire setup and deployment process.
Ensure the video covers:
RabbitMQ/Celery setup.
Python application development.
Nginx configuration.
Sending email via SMTP.
Logging current time.
Exposing the endpoint using ngrok.
Submit the endpoint and screen recording.
Submission Details:
Submission Link: https://forms.gle/okhAFDnXQ5Dw6Ls39
Deadline: Saturday, 12th July 2024, by 11:59 PM GMT.
Submission Requirements:
Provide the ngrok (or equivalent) endpoint for testing.
Submit the screen recording walk-through.
Ensure all requirements are met and the application functions correctly.
Evaluation Criteria:
Functionality: All specified features must work correctly.
Clarity: Code and configurations must be well-documented.
Presentation: The screen recording should be clear and comprehensive.
Deadline Adherence: Strict deadline, no late submissions accepted.
