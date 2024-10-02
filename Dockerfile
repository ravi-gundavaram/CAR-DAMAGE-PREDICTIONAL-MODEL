FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy files
COPY . .

# Expose port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]
