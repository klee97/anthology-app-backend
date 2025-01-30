# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# # Run migrations
# CMD ["sh", "-c", "python manage.py migrate"]
