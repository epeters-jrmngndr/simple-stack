FROM python:3.10-slim

WORKDIR /message

COPY server.py /message
COPY requirements.txt /message
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]