#!/bin/bash


docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

sudo uvicorn app:app --host 0.0.0.0 --port 8000

