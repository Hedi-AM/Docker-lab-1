FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV WELCOME_MESSAGE="Bonjour depuis mon conteneur Docker !"

EXPOSE 5000

CMD ["python", "app.py"]
