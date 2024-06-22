import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("ServiceAccountKey.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://faceregconition-80c55-default-rtdb.firebaseio.com/",
        "storageBucket": "faceregconition-80c55.appspot.com"
    })
