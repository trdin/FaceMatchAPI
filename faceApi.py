# face_recognition_server.py
import face_recognition
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import base64
import cv2
import numpy as np
import matplotlib.pyplot as plt


class FaceRecognitionHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # prejme slike
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        request = json.loads(body)

        face1 = request["face1"]
        # slike pretvori iz json stringa v slike v arrayu
        face1 = base64.b64decode(face1.split(',')[1])
        numpy_array = np.frombuffer(face1, dtype=np.uint8)
        face1 = np.array(cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED))
        face1 = cv2.cvtColor(face1, cv2.COLOR_BGR2RGB)

        plt.imshow(face1)
        plt.show()
        # face2
        face2 = base64.b64decode(request["face2"].split(',')[1])
        numpy_array = np.frombuffer(face2, dtype=np.uint8)
        face2 = np.array(cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED))
        face2 = cv2.cvtColor(face2, cv2.COLOR_BGR2RGB)

        plt.imshow(face2)
        plt.show()

        # preverimo lokacije obrazov
        face1_locations = face_recognition.face_locations(face1)
        face2_locations = face_recognition.face_locations(face2)

        # ce je na kateri sliki vec ko en obraz, ne testiramo
        if len(face1_locations) == 1 and len(face2_locations) == 1:
            # face encodings
            face1_encoded = face_recognition.face_encodings(face1)[0]
            face2_encoded = face_recognition.face_encodings(face2)[0]

            # primerjamo encodinge
            result = face_recognition.compare_faces(
                [face1_encoded], face2_encoded)
            print(result)
        else:
            result = [False]

        # vrnemo rezultat
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        str = 'false'
        if (result[0]):
            str = 'true'
        self.wfile.write(('{"same": "'+str+'"}').encode("utf-8"))


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), FaceRecognitionHandler)
    print('Starting face recognition server on 0.0.0.0:8000...')
    server.serve_forever()
