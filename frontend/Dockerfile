# Use an official Nginx image as the base image
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy the HTML file to the Nginx HTML directory
COPY templates/index.html /usr/share/nginx/html

# Expose port 80 to serve the HTML page
EXPOSE 80

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
