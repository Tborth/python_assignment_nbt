from flask import abort
from flask import jsonify
from functools import wraps
from models import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IntegrityError as e:
            db.session.rollback()
            return jsonify({"error": "Integrity Error", "message": str(e.orig)}), 400
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({"error": "Database Error", "message": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Unexpected Error", "message": str(e)}), 500
    return wrapper


def model_to_dict(instance):
    return {c.name: getattr(instance, c.name) for c in instance.__table__.columns}

