# Use official Python image as a base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Command to run your Flask app
CMD ["python3", "main.py"]
