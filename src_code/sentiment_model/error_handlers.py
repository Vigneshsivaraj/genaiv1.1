from errors.invalid_input_exception import InvalidInputException
from flask import jsonify

def global_error_handler(app):
    @app.errorhandler(InvalidInputException)
    def handle_invalid_input(error):
        return jsonify({"errror_msg":str(error),"status":400}),400