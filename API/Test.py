from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://faceregconition-80c55-default-rtdb.firebaseio.com/"
})

app = Flask(__name__)

students_ref = db.reference('Students')

student_data = students_ref.get()

class_ref = db.reference('Classes')

class_data = class_ref.get()

@app.route('/students', methods=['GET'])
def get_students():
    student_data = students_ref.get()
    return jsonify(student_data), 200

@app.route('/classes', methods=['GET'])
def get_classes():
    class_data = class_ref.get()
    return jsonify(class_data), 200

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    student_info = students_ref.child(student_id).get()
    if student_info:
        return jsonify(student_info), 200
    else:
        return "Student not found", 404
    
@app.route('/classes/<class_id>/students', methods=['GET'])
def get_class_students(class_id):
    class_students = []
    student_data = students_ref.get()
    for student_id, student_info in student_data.items():
        if 'Classes' in student_info and class_id in student_info['Classes']:
            class_students.append({student_id: student_info})
    if class_students:
        return jsonify(class_students), 200
    else:
        return "No students found for this class", 404

@app.route('/students/search', methods=['POST'])
def search_students():
    data = request.get_json()
    if data:
        field = data.get('field')
        value = data.get('value')
        student_data = students_ref.get()
        found_students = [student_info for student_info in student_data.values() if student_info.get(field) == value]
        return jsonify(found_students), 200
    else:
        return "Invalid request data", 400
    

@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    if data:
        student_info = data
        students_ref.child(student_id).update(student_info)
        updated_student_info = students_ref.child(student_id).get() 
        return jsonify(updated_student_info), 200
    else:
        return "Invalid request data", 400

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    students_ref.child(student_id).delete()
    return "Student deleted successfully", 200

if __name__ == "__main__":
    app.run(debug=True)
