# Use an appropriate base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app/

# Copy the wait-for-it.sh script
COPY wait-for-it.sh /wait-for-it.sh

# Make sure the script is executable
RUN chmod +x /wait-for-it.sh

# Set the command to start the service (with wait-for-it.sh)
CMD ["/wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
