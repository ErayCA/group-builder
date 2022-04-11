# Import libraries and define blueprint
from models.models import Project, db
from flask import Blueprint, request
from responses import generateResponse, generateError
project_blueprint = Blueprint('project', __name__)


# Route to get all projects
@project_blueprint.route('/', methods=['GET'])
def get_all_projects():
    try:
        db_projects = Project.query.all()
        projects = []

        for project in db_projects:
            projects.append(Project.jsonify(project))

        return generateResponse(projects)
    except:
        return generateError(500, "Could not process request")


# Routes to handle single project CRUD actions
@project_blueprint.route('/byID/<project_id>', methods=['GET', 'POST', 'DELETE'])
def manage_project(project_id):
    try:
        if (request.method == 'GET'):
            project = Project.query.filter_by(id=project_id).first()

            if (project):
                return generateResponse(Project.jsonify(project))
            else:
                return generateError(404, "Project not found")
        if (request.method == "POST"):
            try:
                project = Project(
                    id=project_id,
                    projectname=request.json["projectname"],
                    managerID=request.json["managerID"],
                    cohortID=request.json["cohortID"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(project)
            db.session.commit()

            return generateResponse("Project created")
        if (request.method == "DELETE"):
            project = Project.query.filter_by(id=project_id).first()
            if (project):
                db.session.delete(project)
                db.session.commit()

                return generateResponse("Project deleted")
            else:
                return generateError(404, "Project not found")
    except:
        return generateError(500, "Could not process request")