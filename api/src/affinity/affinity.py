# Import libraries and define blueprint
from models.models import Affinity, db
from flask import Blueprint, request
from responses import generateResponse, generateError
affinity_blueprint = Blueprint('affinity', __name__)


# Route to get all affinities
@affinity_blueprint.route('/', methods=['GET'])
def get_all_affinities():
    try:
        db_affinities = Affinity.query.all()
        affinities = []

        for affinity in db_affinities:
            affinities.append(Affinity.jsonify(affinity))
        
        return generateResponse(affinities)
    except:
        return generateError(500, "Could not process request")    


# Routes to handle single affinity CRUD actions
@affinity_blueprint.route('/byID/<affinity_id>', methods=['GET', 'POST', 'DELETE'])
def manage_affinity(affinity_id):
    try:
        if (request.method == "GET"):
            affinity = Affinity.query.filter_by(id=affinity_id).first()

            if (affinity):
                return generateResponse(Affinity.jsonify(affinity))
            else:
                return generateError(404, "Affinity not found")
        if (request.method == 'POST'):
            try:
                affinity = Affinity(
                    id=affinity_id,
                    affinityname=request.json["affinityname"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(affinity)
            db.session.commit()
            
            return generateError("Affinity created")
        if (request.method == 'DELETE'):
            affinity = Affinity.query.filter_by(id=affinity_id).first()
            if (affinity):
                db.session.delete(affinity)
                db.session.commit()

                return generateResponse("Affinity deleted")
            else:
                return generateError(404, "Affinity not found")
    except:
        return generateError(500, "Could not process request")