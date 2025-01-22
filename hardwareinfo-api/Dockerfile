FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY . .

# Expose the port used by the Flask application
EXPOSE 5003

# Run the Flask application
CMD ["python", "app.py"]

