import cv2
import dlib
import numpy as np
from deepface import DeepFace
from flask import Flask, request, jsonify
import json
# import tensorflow as tf
from scipy.spatial.distance import cosine

import sys
sys.path.insert(0, 'Silent-Face-Anti-Spoofing-master')
from test import test

app = Flask(__name__)
# Path to the shape predictor file
datFile = "shape_predictor_68_face_landmarks.dat"

# Load the cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load the detector and predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(datFile)

# # Load the model
# model = tf.keras.applications.ResNet50(weights='imagenet')


def detect_faces(img):
    '''The function `detect_faces` takes an image as input, converts it
    to grayscale, detects faces using a cascade classifier, and returns
    a list of coordinates representing the detected faces.
    
    Parameters
    ----------
    img
        The input image on which you want to detect faces.
    
    Returns
    -------
        a list of faces detected in the image.
    '''
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Display the frame

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    # Return the list of faces
    return faces


def align_face(img, face):
    '''The `align_face` function takes an image and a bounding box of a face as input, and aligns the face
    in the image based on the position of the eyes.
    
    Parameters
    ----------
    img
        The input image that contains the face you want to align. It should be in BGR format.
    face
        The "face" parameter is a list containing the coordinates and dimensions of the detected face in
    the image. It should have the format [x, y, width, height], where:
    
    Returns
    -------
        the aligned face image.
    
    '''
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect facial landmarks
    rect = dlib.rectangle(
        int(face[0]), int(face[1]), int(face[0] + face[2]), int(face[1] + face[3])
    )
    shape = predictor(gray, rect)
    shape = np.array(
        [(shape.part(j).x, shape.part(j).y) for j in range(shape.num_parts)]
    )

    # Specify the size of the aligned face image
    desired_face_width = 256
    desired_face_height = desired_face_width

    # Specify the indexes of the facial landmarks
    # for the left eye and the right eye
    left_eye_landmarks = [36, 37, 38, 39, 40, 41]
    right_eye_landmarks = [42, 43, 44, 45, 46, 47]

    # Calculate the center of the left eye and the right eye
    left_eye_center = np.mean(shape[left_eye_landmarks], axis=0).astype(int)
    right_eye_center = np.mean(shape[right_eye_landmarks], axis=0).astype(int)

    # Calculate the angle between the eye centers
    dY = right_eye_center[1] - left_eye_center[1]
    dX = right_eye_center[0] - left_eye_center[0]
    angle = np.degrees(np.arctan2(dY, dX))

    # Calculate the scale of the new resulting image by taking the ratio of
    # the distance between eyes in the current image to the ratio of distance
    # between eyes in the desired image
    dist = np.sqrt((dX**2) + (dY**2))
    desired_dist = (
        desired_face_width * 0.27
    )  # The desired distance is set to be approximately 27% of the face width
    scale = desired_dist / dist

    # Calculate the center of the eyes
    eyes_center = (
        int((left_eye_center[0] + right_eye_center[0]) // 2),
        int((left_eye_center[1] + right_eye_center[1]) // 2),
    )

    # Get the rotation matrix for rotating and scaling the face
    M = cv2.getRotationMatrix2D(eyes_center, angle, scale)

    # Update the translation component of the matrix
    tX = desired_face_width * 0.5
    tY = desired_face_height * 0.3
    M[0, 2] += tX - eyes_center[0]
    M[1, 2] += tY - eyes_center[1]

    # Apply the affine transformation
    (w, h) = (desired_face_width, desired_face_height)
    output = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC)

    return output



def extract_features(face):
    '''The function "extract_features" takes a face image as input, converts it to RGB color format, and
    uses the DeepFace model to predict the embedding of the face.
    
    Parameters
    ----------
    face
        The "face" parameter is an image of a face that you want to extract features from. It is expected
    to be in BGR color format, which is the default color format used by OpenCV.
    
    Returns
    -------
        the embedding of the face, which is a numerical representation of the face's features.

    '''
    # Convert the face to RGB color format
    face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

    # Use the DeepFace model to predict the embedding
    embedding = DeepFace.represent(face_rgb, model_name="Facenet")

    return embedding


def match_face(embedding, database):
    '''The function `match_face` takes an input face embedding and a database of face embeddings, and
    returns the name of the closest matching face in the database if the distance is below a certain
    threshold, otherwise it returns None.
    
    Parameters
    ----------
    embedding
        The embedding parameter is a numerical representation of a face. It is typically a vector of
    numbers that captures the unique features of a face.
    database
        The database parameter is a dictionary that contains the embeddings of known faces. The keys of the
    dictionary are the names of the individuals and the values are the corresponding embeddings.
    
    Returns
    -------
        the name of the closest match in the database if the minimum distance is less than 0.50. Otherwise,
    it returns None.
    
    '''
    min_distance = 100  # Initialize min_distance with a large number
    match = None  # Initialize match with None

    # Loop over all faces in the database
    for name, db_embedding in database.items():
        # Calculate the cosine distance between the input
        # embedding and the database embedding
        distance = cosine(embedding, db_embedding)

        # If the distance is less than the min_distance, update
        # the min_distance and match
        if distance < min_distance:
            min_distance = distance
            match = name

    # If the min_distance is less than a threshold, return the match
    if min_distance < 0.20:
        return match
    else:   
        return None


@app.route('/')
def hello():
    return "Hello this is Face Attendance app"


@app.route('/detect_faces', methods=['POST'])
def detect_faces_route():
    data = request.files['image'].read()
    nparr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    faces = detect_faces(img)
    # Chuyển đổi tuple thành list
    if isinstance(faces, tuple):
        faces = list(faces)

    # Chuyển đổi ndarray thành list
    if isinstance(faces, np.ndarray):
        faces = faces.tolist()

    return jsonify(faces)


@app.route('/align_face', methods=['POST'])
def align_face_route():
    data = request.files['image'].read()
    face = json.loads(request.form['face'])

    nparr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    aligned_face = align_face(img, face)
    if isinstance(aligned_face, np.ndarray):
        aligned_face = aligned_face.tolist()

    return jsonify(aligned_face)


@app.route('/extract_features', methods=['POST'])
def extract_features_route():
    data = request.files['image'].read()
    nparr = np.frombuffer(data, np.uint8)
    face = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    embedding = extract_features(face)
    return jsonify(embedding[0]['embedding'])


@app.route('/match_face', methods=['POST'])
def match_face_route():
    embedding = request.json['embedding']
    database = request.json['database']
    match = match_face(embedding, database)
    return jsonify({"match": match})

@app.route('/anti_spoofing', methods=['POST'])
def anti_spoofing():
    try:
        # Read the image file from the request
        image_file = request.files['image'].read()
        
        # Convert the image bytes to a NumPy array
        nparr = np.frombuffer(image_file, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Call the test function with the required parameters
        model_dir = "Silent-Face-Anti-Spoofing-master/resources/anti_spoof_models"
        label = test(image=frame, model_dir=model_dir, device_id=0)
        label = int(label)
        # Check the label and return the appropriate response
        if label == 1:
            return jsonify({"label": label, "message": "Real face detected"}), 200
        else:
            return jsonify({"label": label, "message": "Spoof face detected"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)