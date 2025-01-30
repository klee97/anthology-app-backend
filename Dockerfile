# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Run migrations and start the server
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
