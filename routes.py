
from flask import request, jsonify
from models import app,db,User,Department,Course,Student,AttendanceLog
from utitlity import model_to_dict,handle_exceptions





@app.route('/users', methods=['POST'])
@handle_exceptions
def create_user():
    data = request.json
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(model_to_dict(user)), 201
   

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([model_to_dict(u) for u in users])

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(model_to_dict(user))

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


# ---------------------------- Department APIs ----------------------------

@app.route('/departments', methods=['POST'])
def create_department():
    data = request.json
    department = Department(**data)
    db.session.add(department)
    db.session.commit()
    return jsonify(model_to_dict(department)), 201

@app.route('/departments', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    return jsonify([model_to_dict(d) for d in departments])

@app.route('/departments/<int:id>', methods=['PUT'])
def update_department(id):
    department = Department.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(department, key, value)
    db.session.commit()
    return jsonify(model_to_dict(department))

@app.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return '', 204


# ---------------------------- Course APIs ----------------------------

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    course = Course(**data)
    db.session.add(course)
    db.session.commit()
    return jsonify(model_to_dict(course)), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([model_to_dict(c) for c in courses])

@app.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    course = Course.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(course, key, value)
    db.session.commit()
    return jsonify(model_to_dict(course))

@app.route('/courses/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return '', 204


# ---------------------------- Student APIs ----------------------------

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    student = Student(**data)
    db.session.add(student)
    db.session.commit()
    return jsonify(model_to_dict(student)), 201

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([model_to_dict(s) for s in students])

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(student, key, value)
    db.session.commit()
    return jsonify(model_to_dict(student))

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return '', 204


# ---------------------------- Attendance Log APIs ----------------------------

@app.route('/attendance', methods=['POST'])
def create_attendance():
    data = request.json
    attendance = AttendanceLog(**data)
    db.session.add(attendance)
    db.session.commit()
    return jsonify(model_to_dict(attendance)), 201

@app.route('/attendance', methods=['GET'])
def get_attendance():
    logs = AttendanceLog.query.all()
    return jsonify([model_to_dict(a) for a in logs])

@app.route('/attendance/<int:id>', methods=['PUT'])
def update_attendance(id):
    attendance = AttendanceLog.query.get_or_404(id)
    for key, value in request.json.items():
        setattr(attendance, key, value)
    db.session.commit()
    return jsonify(model_to_dict(attendance))

@app.route('/attendance/<int:id>', methods=['DELETE'])
def delete_attendance(id):
    attendance = AttendanceLog.query.get_or_404(id)
    db.session.delete(attendance)
    db.session.commit()
    return '', 204