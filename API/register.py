from flask import Flask, request, jsonify
import datetime
import os
import firebase_admin
from firebase_admin import credentials, db, storage

# Khởi tạo thông tin xác thực Firebase từ tệp ServiceAccountKey.json
cred = credentials.Certificate("ServiceAccountKey.json")

# Khởi tạo ứng dụng Firebase với thông tin xác thực và đường dẫn tới Realtime Database và Firebase Storage
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://faceregconition-80c55-default-rtdb.firebaseio.com/",
    "storageBucket": "faceregconition-80c55.appspot.com"
})

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Tham chiếu đến bucket của Firebase Storage
storage_ref = storage.bucket()

# Tham chiếu đến nút 'Students' trong Realtime Database
students_ref = db.reference('Students')

@app.route('/students/<student_id>', methods=['POST'])
def add_student(student_id):
    data = request.get_json()
    if data:
        student_info = {
            'Email': data.get('email'),
            'Faculty': data.get('faculty'),
            'Major': data.get('major'),
            'Name': data.get('name'),
            'Year': data.get('year'),
            'embeddings': data.get('embeddings'),
            'Classes': {}
        }
        
        # Cập nhật thông tin sinh viên
        user_ref = students_ref.child(student_id)
        user_ref.update(student_info)
        
        # Cập nhật thông tin lớp học
        classes = data.get('classes', [])
        for c in classes:
            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d %H:%M:%S")
            class_ref = user_ref.child('Classes').child(c)
            class_ref.update({
                'AttendanceCount': '0',
                'Datetime': date
            })
        
        return "Student added successfully", 200
    else:
        return "Invalid request data", 400

@app.route('/images/<student_id>', methods=['POST'])
def upload_file(student_id):
    # Kiểm tra xem yêu cầu có chứa file không
    if 'file' not in request.files:
        return "No file part", 400
    
    # Lấy file từ yêu cầu
    file = request.files['file']
    
    # Kiểm tra xem có file được chọn không
    if file.filename == '':
        return "No selected file", 400
    
    # Lấy phần mở rộng của tên tệp
    file_name, file_extension = os.path.splitext(file.filename)
    
    # Kết nối tới Firebase Storage
    blob = storage_ref.blob(f'images/{student_id}{file_extension}')  # Đường dẫn tới tệp trên Firebase Storage

    # Tải tệp lên Firebase Storage
    blob.upload_from_file(file)

    return "File uploaded successfully", 200

if __name__ == "__main__":
    app.run(debug=True)
