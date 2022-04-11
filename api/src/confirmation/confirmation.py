# Import libraries and define blueprint
from models.models import Confirmation, db
from flask import Blueprint, request
from responses import generateResponse, generateError
confirmation_blueprint = Blueprint('confirmation', __name__)


# Route to get all confirmations
@confirmation_blueprint.route('/', methods=['GET'])
def get_all_confirmations():
    try:
        db_confirmations = Confirmation.query.all()
        confirmations = []

        for confirmation in db_confirmations:
            confirmations.append(Confirmation.jsonify(confirmation))

        return generateResponse(confirmations)
    except:
        return generateError(500, "Could not process request")


# Routes to handle single confirmation CRUD actions
@confirmation_blueprint.route('/byID/<confirmation_id>', methods=['GET', 'POST', 'DELETE'])
def manage_confirmation(confirmation_id):
    try:
        if (request.method == "GET"):
            confirmation = Confirmation.query.filter_by(
                id=confirmation_id).first()

            if (confirmation):
                return generateResponse(Confirmation.jsonify(confirmation))
            else:
                return generateError(404, "Confirmation not found")
        if (request.method == 'POST'):
            try:
                confirmation = Confirmation(
                    id=confirmation_id,
                    confirmationname=request.json["confirmationname"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(confirmation)
            db.session.commit()

            return generateError("Confirmation created")
        if (request.method == 'DELETE'):
            confirmation = Confirmation.query.filter_by(
                id=confirmation_id).first()
            if (confirmation):
                db.session.delete(confirmation)
                db.session.commit()

                return generateResponse("Confirmation deleted")
            else:
                return generateError(404, "Confirmation not found")
    except:
        return generateError(500, "Could not process request")