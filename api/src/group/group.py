# Import libraries and define blueprint
from models.models import Group, GroupMember, User, db
from flask import Blueprint, request, make_response
from responses import generateResponse, generateError
group_blueprint = Blueprint('group', __name__)


# Route to get all groups
@group_blueprint.route('/', methods=['GET'])
def get_all_groups():
    try:
        db_groups = Group.query.all()
        groups = []

        for group in db_groups:
            groups.append(Group.jsonify(group))

        return generateResponse(groups)
    except:
        return generateError(500, "Could not proccess request")


# Routes to handle single group CRUD actions
@group_blueprint.route('/byID/<group_id>', methods=['GET', 'POST', 'DELETE'])
def manage_group(group_id):
    try:
        if (request.method == 'GET'):
            group = Group.query.filter_by(id=group_id).first()

            if (group):
                return generateResponse(Group.jsonify(group))
            else:
                return generateError(404, "Group not found")
        if (request.method == 'POST'):
            try:
                group = Group(
                    id=group_id,
                    groupname=request.json["groupname"],
                    groupprojectID=request.json["groupprojectID"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(group)
            db.session.commit()

            return generateResponse("Group created")
        if (request.method == 'DELETE'):
            group = Group.query.filter_by(id=group_id).first()
            if (group):
                db.session.delete(group)
                db.session.commit()

                return generateResponse("Group deleted")
            else:
                return generateError(404, "Group not found")
    except:
        return generateError(500, "Could not proccess request")


# Route to handle getting all users in group
@group_blueprint.route('/studentList/<group_id>', methods=['GET'])
def get_users(group_id):
    try:
        group = Group.query.filter_by(id=group_id).first()

        if(group):

            groupmembers = []
            groupmembers = get_groupmembers(group_id)

            users = []
            for groupmember in groupmembers:
                user_id = groupmember.groupmemberuserID
                user = User.query.filter_by(id=user_id).first()
                users.append(User.jsonify(user))
        
            return generateResponse(users)

        else:
            return generateError(404, "Group not found")
    except:
        return generateError(500, "Could not process request")


# Helper function to fetch all groupmembers for a group
def get_groupmembers(group_id):
    groupmembers = []
    groupmembers = GroupMember.query.filter(GroupMember.groupmembergroupID.contains(group_id)).all()

    return groupmembers