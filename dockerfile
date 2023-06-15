# Use an official Python runtime as a parent image

# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the application port (change it if necessary)
EXPOSE 5000

# Run the application
CMD ["python", "flask_app.py"]


