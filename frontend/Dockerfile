# Use the official Nginx image as the base image
FROM nginx:alpine

# Copy the contents of the frontend folder to the default Nginx public directory
COPY frontend .

# Expose port 80 to the outer world
EXPOSE 80

# The container starts Nginx when it runs
CMD ["nginx", "-g", "daemon off;"]
