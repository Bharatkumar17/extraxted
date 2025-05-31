FROM python:3.9.7-slim-buster

WORKDIR .
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3 main.py"]
services:
  your-bot-service:
    # ...
    command: python3 -u main.py  # "-u" for unbuffered logs
