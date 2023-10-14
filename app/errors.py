from flask import jsonify

def error_response(status_code, message=None):
    if message:
        payload = {'error': message}
    else:
        payload = {'error': 'Something went wrong'}

    response = jsonify(payload)
    response.status_code = status_code
    return response