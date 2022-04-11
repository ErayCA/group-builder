# Import libraries and define blueprint
from models.models import GroupMember, db
from flask import Blueprint, request, make_response
from responses import generateResponse, generateError
groupmember_blueprint = Blueprint('groupmember', __name__)


# Route to get all groupmembers
@groupmember_blueprint.route('/', methods=['GET'])
def get_all_groupmembers():
    try:
        db_groupmembers = GroupMember.query.all()
        groupmembers = []

        for groupmember in db_groupmembers:
            groupmembers.append(GroupMember.jsonify(groupmember))

        return generateResponse(groupmembers)
    except:
        return generateError(500, "Could not proccess request")


# Routes to handle single groupmember CRUD actions
@groupmember_blueprint.route('/byID/<groupmember_id>', methods=['GET', 'POST', 'DELETE'])
def manage_groupmember(groupmember_id):
    try:
        if (request.method == 'GET'):
            groupmember = GroupMember.query.filter_by(id=groupmember_id).first()

            if (groupmember):
                return generateResponse(GroupMember.jsonify(groupmember))
            else:
                return generateError(404, "GroupMember not found")
        if (request.method == 'POST'):
            try:
                groupmember = GroupMember(
                    id=groupmember_id,
                    groupmemberuserID=request.json["groupmemberuserID"],
                    groupmembergroupID=request.json["groupmembergroupID"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(groupmember)
            db.session.commit()

            return generateResponse("GroupMember created")
        if (request.method == 'DELETE'):
            groupmember = GroupMember.query.filter_by(id=groupmember_id).first()
            if (groupmember):
                db.session.delete(groupmember)
                db.session.commit()

                return generateResponse("GroupMember deleted")
            else:
                return generateError(404, "GroupMember not found")
    except:
        return generateError(500, "Could not proccess request")