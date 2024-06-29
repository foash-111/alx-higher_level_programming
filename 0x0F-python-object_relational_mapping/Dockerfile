# # Use an official Ubuntu 22.04 LTS image as a parent image
# FROM ubuntu:22.04

# # Set environment variables
# ENV DEBIAN_FRONTEND=noninteractive

# # Install required packages
# RUN apt-get update && apt-get install -y \
#     python3 \
#     python3-pip \
#     git \
#     mysql-client \
#     libmysqlclient-dev

# # Upgrade pip
# RUN pip3 install --no-cache-dir --upgrade pip

# # Install SQLAlchemy and other Python dependencies
# RUN pip3 install --no-cache-dir \
#     sqlalchemy \
#     mysqlclient \
#     flask  # Example additional dependencies

# # Install the required libraries for MySQL client
# RUN apt-get update && apt-get install -y \
#     default-libmysqlclient-dev build-essential \
#     && rm -rf /var/lib/apt/lists/*

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Expose the port your app runs on
# EXPOSE 5000

# # Default command to run your app
# CMD ["python3", "app.py"]
#------------------------

# Use the official Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install MySQL client dependencies
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

RUN pip3 install --no-cache-dir \
    sqlalchemy \
    mysqlclient \
    flask \
    git


RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/*



RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Set the default command to run Flask
CMD ["flask", "run", "--host=0.0.0.0"]
