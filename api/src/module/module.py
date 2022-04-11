# Import libraries and define blueprint
from models.models import Module, db
from flask import Blueprint, request, make_response
from responses import generateResponse, generateError
module_blueprint = Blueprint('module', __name__)


# Route to get all modules
@module_blueprint.route('/', methods=['GET'])
def get_all_modules():
    try:
        db_modules = Module.query.all()
        modules = []

        for module in db_modules:
            modules.append(Module.jsonify(module))

        return generateResponse(modules)
    except:
        return generateError(500, "Could not proccess request")


# Routes to handle single module CRUD actions
@module_blueprint.route('/byID/<module_id>', methods=['GET', 'POST', 'DELETE'])
def manage_module(module_id):
    try:
        if (request.method == 'GET'):
            module = Module.query.filter_by(id=module_id).first()

            if (module):
                return generateResponse(Module.jsonify(module))
            else:
                return generateError(404, "Module not found")
        if (request.method == 'POST'):
            try:
                module = Module(
                    id=module_id,
                    modulename=request.json["modulename"],
                    moduleleaderID=request.json["moduleleaderID"],
                    modulecohortID=request.json["modulecohortID"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(module)
            db.session.commit()

            return generateResponse("Module created")
        if (request.method == 'DELETE'):
            module = Module.query.filter_by(id=module_id).first()
            if (module):
                db.session.delete(module)
                db.session.commit()

                return generateResponse("Module deleted")
            else:
                return generateError(404, "Module not found")
    except:
        return generateError(500, "Could not proccess request")