# Use a minimal base image
FROM python:3.9-alpine

COPY requirements.txt .

WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python modules listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the C source code into the container
COPY networking.py .

# Define the command to run when the container starts
CMD ["python", "networking.py"]
