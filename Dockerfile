# Use an official Ubuntu 20.04 LTS image as a parent image
FROM ubuntu

# Set the working directory to /app
WORKDIR /app

# # Update packages and install necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip nginx git npm nodejs openssh-server sudo

RUN npm install -g n
RUN n stable

RUN npm install --global yarn

RUN yarn global add wetty
# COPY ~/.config/yarn/global/node_modules/wetty/conf/wetty.conf /etc/init

# Copy the current directory contents into the container at /app
COPY . .
ENV FLASK_ENV production
# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN apk update && apk add nginx
# RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
# Copy the ssh public key in the authorized_keys file. The idkey.pub below is a public key file you get from ssh-keygen. They are under ~/.ssh directory by default.
# Start SSH service
# RUN service ssh start
# Expose docker port 22
EXPOSE 22
CMD ["service", "ssh", "start"]

# CMD ["nginx", "-g", "daemon off;"]
# Run app.py when the container launches
# CMD ["flask", "--app", "web/app", "run"]
