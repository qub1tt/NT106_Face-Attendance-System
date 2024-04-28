# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import storage
# from firebase_admin import auth
# import firebase_admin.auth
import requests 
# cred = credentials.Certificate("ServiceAccountKey.json")

# firebase_admin.initialize_app(cred, {"databaseURL":"https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                     
#                                      "storageBucket":"faceregconition-80c55.appspot.com"})


# def login():
#     print("Login...")
#     email = input("Enter email: ")
#     password = input("Enter password: ")
#     try:
#         # Xác thực người dùng bằng email và mật khẩu
#         user = auth.get_user_by_email(email)
        
#         print("Login successful")
#     except :
#         # Xử lý lỗi khi không thể xác thực người dùng
#         print("Invalid email or password:")



def authenticate_with_email_and_password(email, password):
    # lên đồ án lấy
    api_key = "AIzaSyBsKV9779frJjdkuYBMrI2c10Ie3Ubdd5w"
    request_data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"

    response = requests.post(url, json=request_data)
    if response.ok:
        user_data = response.json()
        id_token = user_data.get("idToken")
        print("Đăng nhập thành công!")
        return id_token
    else:
        error_message = response.json().get("error", {}).get("message")
        print("Đăng nhập không thành công:", error_message)
        return None

email = input("Nhập email: ")
password = input("Nhập mật khẩu: ")
id_token = authenticate_with_email_and_password(email, password)

# def signup():
#     print("Sign up...")
#     email = input("Enter email: ")
#     password = input("Enter password: ")
#     try:
#         user= auth.create_user(email=email,password=password)
#         print("user created successfully")
#     except:
#         print("email already exist")
   

# ans = input("Are you a new user? [y/n]: ")
# if ans == 'n':
#     authenticate_with_email_and_password()
# elif ans == 'y':
#     signup()
