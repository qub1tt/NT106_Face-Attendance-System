# firebase_config.py
import firebase_admin
from firebase_admin import credentials, db

# Ensure Firebase is only initialized once
if not firebase_admin._apps:
    cred = credentials.Certificate("ServiceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://faceregconition-80c55-default-rtdb.firebaseio.com/",
        "storageBucket": "faceregconition-80c55.appspot.com"
    })

class_ref = db.reference('Classes')
students_ref = db.reference('Students')
