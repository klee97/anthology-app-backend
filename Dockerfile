# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django app into the container
COPY . .

# Expose the Django default port
EXPOSE 8000

# Run migrations and start the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
