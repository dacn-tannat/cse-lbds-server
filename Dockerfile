FROM python:3.10-slim

WORKDIR /app

# Cài đặt thư viện hệ thống để kết nối với PostgreSQL (no need?)
# RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Mở port cho FastAPI
EXPOSE 8000

# Chạy ứng dụng bằng uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]