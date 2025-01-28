# Step 1: Use an official Python image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /usr/src/app

# Step 3: Copy the setup script and install dependencies (Bash + Python)
COPY setup.sh ./
RUN chmod +x setup.sh && ./setup.sh

# Step 4: Copy the app files (HTML, CSS, Python code)
COPY ./app ./app
COPY server.py .
COPY requirements.txt .

# Step 5: Install Python dependencies
RUN pip install -r requirements.txt

# Step 6: Expose the port Flask will run on
EXPOSE 5000

# Step 7: Define the default command to run the Flask server
CMD ["python", "server.py"]
