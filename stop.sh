#!/bin/bash


# Stop and remove RabbitMQ container
docker stop rabbitmq
docker rm rabbitmq



# Stop Uvicorn server
ps aux | grep '[u]vicorn' | awk '{print $2}' | xargs -r kill

# Stop Python consumer script
ps aux | grep '[c]onsumer.py' | awk '{print $2}' | xargs -r kill