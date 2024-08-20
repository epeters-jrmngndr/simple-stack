#!/bin/bash
docker build -t jrmngndr/message-api:latest . --no-cache
docker push jrmngndr/message-api:latest
