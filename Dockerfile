FROM python:3.11.9-slim

# Install curl (REQUIRED - scraper.py uses curl via subprocess)
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Run the main bot
CMD ["python", "main.py"]
