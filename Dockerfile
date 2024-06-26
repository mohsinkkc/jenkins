FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY program.py /app/

# Expose the port your Python application listens on
EXPOSE 8080

# Command to run the Python script
CMD ["python", "program.py"]
