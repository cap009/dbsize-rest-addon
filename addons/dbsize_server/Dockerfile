FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir flask mysql-connector-python

CMD ["python3", "app.py"]
