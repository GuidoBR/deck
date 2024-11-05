FROM python:3.11-slim

ENV ENVIRONMENT=dev

COPY backend_service/config/dev.env .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /backend_service

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

