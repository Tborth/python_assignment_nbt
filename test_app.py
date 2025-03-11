import pytest
from apps import app,db

# ---------------------- Pytest Fixtures ---------------------- #

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory DB for tests
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests


# ---------------------- User Test Cases ---------------------- #

def test_create_user(client):
    response = client.post('/users', json={
        'type': 'Admin',
        'full_name': 'John Doe',
        'username': 'john',
        'email': 'john@example.com',
        'password': 'securepass',
        'submitted_by': 'admin'
    })
    assert response.status_code == 201
    assert response.json['username'] == 'john'


def test_get_users(client):
    # Pre-create user
    client.post('/users', json={
        'type': 'Admin',
        'full_name': 'John Doe',
        'username': 'john',
        'email': 'john@example.com',
        'password': 'securepass',
        'submitted_by': 'admin'
    })
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) == 1


# ---------------------- Department Test Cases ---------------------- #

def test_create_department(client):
    response = client.post('/departments', json={
        'department_name': 'Computer Science',
        'submitted_by': 'admin'
    })
    assert response.status_code == 201
    assert response.json['department_name'] == 'Computer Science'


def test_get_departments(client):
    client.post('/departments', json={
        'department_name': 'Computer Science',
        'submitted_by': 'admin'
    })
    response = client.get('/departments')
    assert response.status_code == 200
    assert len(response.json) == 1


# ---------------------- Course Test Cases ---------------------- #

def test_create_course(client):
    # Pre-create department
    client.post('/departments', json={'department_name': 'CS', 'submitted_by': 'admin'})

    response = client.post('/courses', json={
        'course_name': 'Python 101',
        'department_id': 1,
        'semester': 'Fall',
        'class_name': 'A',
        'lecture_hours': 40,
        'submitted_by': 'admin',
        'updated_by': 'admin'
    })
    assert response.status_code == 201
    assert response.json['course_name'] == 'Python 101'


def test_get_courses(client):
    client.post('/departments', json={'department_name': 'CS', 'submitted_by': 'admin'})
    client.post('/courses', json={
        'course_name': 'Python 101',
        'department_id': 1,
        'semester': 'Fall',
        'class_name': 'A',
        'lecture_hours': 40,
        'submitted_by': 'admin',
        'updated_by': 'admin'
    })
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.json) == 1


# ---------------------- Student Test Cases ---------------------- #

def test_create_student(client):
    # Pre-create department
    client.post('/departments', json={'department_name': 'IT', 'submitted_by': 'admin'})

    response = client.post('/students', json={
        'full_name': 'Jane Smith',
        'department_id': 1,
        'class_name': 'B',
        'submitted_by': 'admin',
        'updated_by': 'admin'
    })
    assert response.status_code == 201
    assert response.json['full_name'] == 'Jane Smith'


def test_get_students(client):
    client.post('/departments', json={'department_name': 'IT', 'submitted_by': 'admin'})
    client.post('/students', json={
        'full_name': 'Jane Smith',
        'department_id': 1,
        'class_name': 'B',
        'submitted_by': 'admin',
        'updated_by': 'admin'
    })
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.json) == 1


# ---------------------- Attendance Log Test Cases ---------------------- #

def test_create_attendance(client):
    # Pre-create department, student, course
    client.post('/departments', json={'department_name': 'Math', 'submitted_by': 'admin'})
    client.post('/students', json={
        'full_name': 'Tom Brown',
        'department_id': 1,
        'class_name': 'C',
        'submitted_by': 'admin',
        'updated_by': 'admin'
    })
    client.post('/courses', json={
        'course_name': 'Algebra',
        'department_id': 1,
        'semester': 'Spring',
        'class_name': 'C',
        'lecture_hours': 30,
        'submitted_by': 'admin',
        'updated_by': 'admin'
    })

    response = client.post('/attendance', json={
        'student_id': 1,
        'course_id': 1,
        'present': True,
        'submitted_by': 'admin'
    })
    assert response.status_code == 201
    assert response.json['present'] is True


def test_get_attendance(client):
    client.post('/departments', json={'department_name': 'Math', 'submitted_by': 'admin'})
    client.post('/students', json={
        'full_name': 'Tom Brown',
        'department_id': 1,
        'class_name': 'C',
        'submitted_by': 'admin',
        'updated_by': 'admin'
    })
    client.post('/courses', json={
        'course_name': 'Algebra',
        'department_id': 1,
        'semester': 'Spring',
        'class_name': 'C',
        'lecture_hours': 30,
        'submitted_by': 'admin',
        'updated_by': 'admin'
    })
    client.post('/attendance', json={
        'student_id': 1,
        'course_id': 1,
        'present': True,
        'submitted_by': 'admin'
    })
    response = client.get('/attendance')
    assert response.status_code == 200
    assert len(response.json) == 1

