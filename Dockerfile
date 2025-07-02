FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y gcc build-essential libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 10000

CMD ["python", "app.py"]
