# Import libraries and define blueprint
from models.models import Link, db
from flask import Blueprint, request
from responses import generateResponse, generateError
link_blueprint = Blueprint('link', __name__)


# Route to get all links
@link_blueprint.route('/', methods=['GET'])
def get_all_links():
    try:
        db_links = Link.query.all()
        links = []

        for link in db_links:
            links.append(Link.jsonify(link))

        return generateResponse(links)
    except:
        return generateError(500, "Could not process request")


# Routes to handle single link CRUD actions
@link_blueprint.route('/byID/<link_id>', methods=['GET', 'POST', 'DELETE'])
def manage_link(link_id):
    try:
        if (request.method == "GET"):
            link = Link.query.filter_by(id=link_id).first()

            if (link):
                return generateResponse(Link.jsonify(link))
            else:
                return generateError(404, "Link not found")
        if (request.method == 'POST'):
            try:
                link = Link(
                    id=link_id,
                    linkerID=request.json["linkerID"],
                    linkeeID=request.json["linkeeID"],
                    linkprojectID=request.json["linkprojectID"],
                    linkconfirmationID=request.json["linkconfirmationID"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(link)
            db.session.commit()

            return generateResponse("Link created")
        if (request.method == 'DELETE'):
            link = Link.query.filter_by(id=link_id).first()
            if (link):
                db.session.delete(link)
                db.session.commit()

                return generateResponse("Link deleted")
            else:
                return generateError(404, "Link not found")
    except:
        return generateError(500, "Could not process request")