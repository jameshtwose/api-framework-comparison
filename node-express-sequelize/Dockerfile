# Use the official Node.js hydrogen-alpine3.19 image as the base image
FROM node:hydrogen-alpine3.19

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the API will run
EXPOSE 8082

# Start the API
CMD ["npm", "start"]
