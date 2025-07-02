FROM python:3.11-slim

# Установка зависимостей WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libffi-dev \
    libxml2 \
    libgdk-pixbuf2.0-0 \
    libjpeg-dev \
    zlib1g-dev \
    libssl-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /app

# Копирование файлов
COPY . .

# Установка Python-зависимостей
RUN pip install --upgrade pip && pip install -r requirements.txt

# Создание папки для PDF-файлов
RUN mkdir -p generated

# Запуск uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
