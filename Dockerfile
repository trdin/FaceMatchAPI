FROM python:3.9

RUN apt-get update && apt-get install -y cmake

RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy the required files into the container
COPY faceApi.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "./faceApi.py"]