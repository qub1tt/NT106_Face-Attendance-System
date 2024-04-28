import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from firebase_admin import auth

cred = credentials.Certificate("ServiceAccountKey.json")

firebase_admin.initialize_app(cred, {"databaseURL":"https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                     
                                     "storageBucket":"faceregconition-80c55.appspot.com"})