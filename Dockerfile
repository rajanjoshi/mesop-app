# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose the port App Runner expects
EXPOSE 8080

# Run the Mesop app
CMD ["mesop", "serve"]
