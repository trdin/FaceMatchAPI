# Face Recognition Server API

This is a simple API that uses the face_recognition Python library to compare faces. It provides a single endpoint that accepts two images and returns whether they are the same person or not.

Created with [face_recognition library](https://github.com/ageitgey/face_recognition)

## Usage

To use this API, you can send a POST request to the /compare endpoint with two images in Base64 format. The API will then return a JSON object with a same field set to true or false depending on whether the faces in the images match or not.

### Example Request7

```python
import requests
import base64

with open("face1.jpg", "rb") as image_file:
    encoded_string1 = base64.b64encode(image_file.read())

with open("face2.jpg", "rb") as image_file:
    encoded_string2 = base64.b64encode(image_file.read())

payload = {
    "face1": encoded_string1.decode(),
    "face2": encoded_string2.decode()
}

response = requests.post("http://localhost:8000/compare", json=payload)

print(response.json())

```

### Example Response

```json
{
    "same": "true"
}

```

## Running the API

To run this API, you can use Docker Compose. Simply run the following command in the root directory of this project:

```
docker-compose up -d --build
```

This will build the Docker image and start the container in the background.

The API will be available at [http://localhost:8000/compare](http://localhost:8000/compare).

## Requirements
- Python 3.9
- face_recognition library
- OpenCV library
- Matplotlib library
- Docker and Docker Compose (if running with Docker)
