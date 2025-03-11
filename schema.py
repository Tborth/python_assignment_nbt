# User Schema
from apps import ma
from models import User,Department,Course,Student,AttendanceLog
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Department Schema
class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department

# Course Schema
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

# Student Schema
class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student

# AttendanceLog Schema
class AttendanceLogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AttendanceLog

# Initialize schema instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

attendance_schema = AttendanceLogSchema()
attendances_schema = AttendanceLogSchema(many=True)
