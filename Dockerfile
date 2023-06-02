# Use an official Ubuntu 20.04 LTS image as a parent image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# # Update packages and install necessary dependencies
# RUN apt-get update && \
#     apt-get install -y python3 python3-pip

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["flask", "--app", "web/app", "run"]
