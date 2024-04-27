from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

# Khởi tạo Firebase với tệp JSON chứa khóa xác thực
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://faceregconition-80c55-default-rtdb.firebaseio.com/"
})

app = Flask(__name__)

students_ref = db.reference('Students')

student_data = students_ref.get()

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(student_data), 200

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    student_info = student_data.get(student_id)
    if student_info:
        return jsonify(student_info), 200
    else:
        return "Student not found", 404

# @app.route('/students/search', methods=['POST'])
# def search_students():
#     data = request.get_json()
#     if data:
#         field = data.get('field')
#         value = data.get('value')
#         found_students = [student_info for student_info in student_data.values() if student_info.get(field) == value]
#         return jsonify(found_students), 200
#     else:
#         return "Invalid request data", 400

# @app.route('/students', methods=['POST'])
# def create_student():
#     data = request.get_json()
#     if data:
#         student_id = data.get('student_id')
#         student_info = data.get('student_info')
#         students_ref.child(student_id).set(student_info)
#         return "Student created successfully", 201
#     else:
#         return "Invalid request data", 400

# @app.route('/students/<student_id>', methods=['PUT'])
# def update_student(student_id):
#     data = request.get_json()
#     if data:
#         student_info = data.get('student_info')
#         students_ref.child(student_id).update(student_info)
#         return "Student updated successfully", 200
#     else:
#         return "Invalid request data", 400

# @app.route('/students/<student_id>', methods=['DELETE'])
# def delete_student(student_id):
#     students_ref.child(student_id).delete()
#     return "Student deleted successfully", 200

if __name__ == "__main__":
    app.run(debug=True)
