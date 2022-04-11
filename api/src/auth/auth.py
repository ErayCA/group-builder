# Import libraries and define blueprint
from models.models import User, db
from flask import Blueprint, request
from responses import generateResponse, generateError
auth_blueprint = Blueprint('auth', __name__)


# Route to register user
@auth_blueprint.route('/register', methods=['POST'])
def register():
    try:
        if (request.method == 'POST'):
            # Check request body for required paramaters
            user_id = None
            password = None

            try:
                user_id=request.json["user_id"]
                password=request.json["new_password"]
            except:
                return generateError(400, "Missing mandatory request paramaters. Mandatory paramaters are user_id and new_password")

            # Search db for user and verify if eligible for registration
            user = None
            try:
                user = User.query.filter_by(id=user_id).first()
            except:
                return generateError(404, "Could not find user by user_id")

            if (user.registered == True):
                return generateError(409, "User already registered")

            user.password = password
            user.registered = True

            db.session.add(user)
            db.session.commit()

            return generateResponse("Registration completed")
    except:
        return generateError(500, "Could not proccess request")