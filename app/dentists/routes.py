from flask import request, jsonify
from app.dentists import bp
from app import db
from app.models import Dentists
from app.schemas import DentistsSchema
from marshmallow import ValidationError
from app.errors import error_response

# [GET] dentists
@bp.route('/', methods=['GET'])
def get_dentists():
    # Fetch all dentist records
    dentists = Dentists.query.all()

    if dentists:
        # Use the schema to serialize the list of dentists
        schema = DentistsSchema(many=True)  # Note the `many=True` because it's a list of records
        return jsonify(schema.dump(dentists))
    else:
        return error_response(404, "No dentists found")

# [POST] dentist
@bp.route('/', methods=['POST'])
def add_dentist():
    schema = DentistsSchema()
    try:
        dentist_data = schema.load(request.json)
        new_dentist = Dentists(**dentist_data)
        db.session.add(new_dentist)
        db.session.commit()
        return schema.dump(new_dentist), 201
    except ValidationError as e:
        return error_response(400, e.messages)
    except Exception as e:
        db.session.rollback()
        return error_response(500, str(e))

# [GET] dentist
@bp.route('/<int:dentist_id>', methods=['GET'])
def get_dentist(dentist_id):

    dentist = Dentists.query.get(dentist_id)

    if dentist:
        schema = DentistsSchema()
        return schema.dump(dentist)
    else:
        return error_response(404, "Dentist not found")

# [DELETE] dentist
@bp.route('/<int:dentist_id>', methods=['DELETE'])
def delete_dentist(dentist_id):

    dentist = Dentists.query.get(dentist_id)
    
    if dentist:
        try:
            db.session.delete(dentist)
            db.session.commit()    
            return jsonify({'message': 'Dentist deleted successfully'}), 200
        
        except Exception as e:
            db.session.rollback()
            return error_response(500, str(e))
    else:
        return error_response(404, "Dentist not found")
