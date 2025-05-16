# FROM python:3.10-slim

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     gcc \
#     libc-dev \
#     tzdata \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt /app/requirements.txt
# WORKDIR /app
# RUN pip install -r requirements.txt


FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY . .

ENV TZ=UTC

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]