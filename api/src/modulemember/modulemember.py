# Import libraries and define blueprint
from models.models import ModuleMember, db
from flask import Blueprint, request, make_response
from responses import generateResponse, generateError
modulemember_blueprint = Blueprint('modulemember', __name__)


# Route to get all modulemembers
@modulemember_blueprint.route('/', methods=['GET'])
def get_all_modulemembers():
    try:
        db_modulemembers = ModuleMember.query.all()
        modulemembers = []

        for modulemember in db_modulemembers:
            modulemembers.append(ModuleMember.jsonify(modulemember))

        return generateResponse(modulemembers)
    except:
        return generateError(500, "Could not proccess request")


# Routes to handle single modulemember CRUD actions
@modulemember_blueprint.route('/byID/<modulemember_id>', methods=['GET', 'POST', 'DELETE'])
def manage_modulemember(modulemember_id):
    try:
        if (request.method == 'GET'):
            modulemember = ModuleMember.query.filter_by(id=modulemember_id).first()

            if (modulemember):
                return generateResponse(ModuleMember.jsonify(modulemember))
            else:
                return generateError(404, "ModuleMember not found")
        if (request.method == 'POST'):
            try:
                modulemember = ModuleMember(
                    id=modulemember_id,
                    modulememberuserID=request.json["modulememberuserID"],
                    modulemembermoduleID=request.json["modulemembermoduleID"],
                    modulememberorder=request.json["modulememberorder"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(modulemember)
            db.session.commit()

            return generateResponse("ModuleMember created")
        if (request.method == 'DELETE'):
            modulemember = ModuleMember.query.filter_by(id=modulemember_id).first()
            if (modulemember):
                db.session.delete(modulemember)
                db.session.commit()

                return generateResponse("ModuleMember deleted")
            else:
                return generateError(404, "ModuleMember not found")
    except:
        return generateError(500, "Could not proccess request")