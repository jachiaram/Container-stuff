# Use a minimal base image with a C compiler
FROM alpine:latest

# Install build essentials (including gcc)
RUN apk add --no-cache build-base

# Copy the C source code into the container
COPY main.C /app/main.C

# Compile the C program
WORKDIR /app
RUN g++ -o main.bin main.C

# Define the command to run when the container starts
CMD ["./main.bin"]
