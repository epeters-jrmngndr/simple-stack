FROM alpine:3.14

WORKDIR /message

COPY server.py /message
COPY requirements.txt /message
RUN apk add python3
RUN apk add curl
RUN python3 -m ensurepip
RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]