# Use the official Nginx image as the base image
FROM nginx:alpine

# Copy the contents of the frontend folder 
COPY index.html /usr/share/nginx/html

# Expose port 80 to the outer world
EXPOSE 80

# The container starts Nginx when it runs
CMD ["nginx", "-g", "daemon off;"]
