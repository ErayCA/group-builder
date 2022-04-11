# Import libraries and define blueprint
from models.models import Like, db
from flask import Blueprint, request
from responses import generateResponse, generateError
like_blueprint = Blueprint('like', __name__)


# Route to get all likes
@like_blueprint.route('/', methods=['GET'])
def get_all_likes():
    try:
        db_likes = Like.query.all()
        likes = []

        for like in db_likes:
            likes.append(Like.jsonify(like))
    
        return generateResponse(likes)
    except:
        return generateError(500, "Could not process request")


# Routes to handle single like CRUD actions
@like_blueprint.route('/byID/<like_id>', methods=['GET', 'POST', 'DELETE'])
def manage_like(like_id):
    try:
        if (request.method == "GET"):
            like = Like.query.filter_by(id=like_id).first()

            if (like):
                return generateResponse(Like.jsonify(like))
            else:
                return generateError(404, "Like not found")
        if (request.method == 'POST'):
            try:
                like = Like(
                    id=like_id,
                    likeaffinityID=request.json["likeaffinityID"],
                    likerID=request.json["likerID"],
                    likeeID=request.json["likeeID"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(like)
            db.session.commit()

            return generateResponse("Like created")
        if (request.method == 'DELETE'):
            like = Like.query.filter_by(id=like_id).first()
            if (like):
                db.session.delete(like)
                db.session.commit()

                return generateResponse("Like deleted")
            else:
                return generateError(404, "Like not found")
    except:
        return generateError(500, "Could not process request")