# Use a lightweight and modern Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=3000 \
    HOST=0.0.0.0

# Set working directory
WORKDIR /app

# Install system dependencies for boto3 + SSL
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port Mesop listens on
EXPOSE 3000

# Command for App Runner to start the app
CMD ["python", "app.py"]
