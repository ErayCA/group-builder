# Import libraries and define blueprint
from models.models import Cohort, db
from flask import Blueprint, request
from responses import generateResponse, generateError
cohort_blueprint = Blueprint('cohort', __name__)


# Route to get all cohorts
@cohort_blueprint.route('/', methods=['GET'])
def get_all_cohorts():
    try:
        db_cohorts = Cohort.query.all()
        cohorts = []

        for cohort in db_cohorts:
            cohorts.append(Cohort.jsonify(cohort))

        return generateResponse(cohorts)
    except:
        return generateError(500, "Could not proccess request")


# Routes to handle single cohort CRUD actions
@cohort_blueprint.route('/byID/<cohort_id>', methods=['GET', 'POST', 'DELETE'])
def manage_cohort(cohort_id):
    try:
        if (request.method == "GET"):
            cohort = Cohort.query.filter_by(id=cohort_id).first()

            if (cohort):
                return generateResponse(Cohort.jsonify(cohort))
            else:
                return generateError(404, "Cohort not found")
        if (request.method == 'POST'):
            try:
                cohort = Cohort(
                    id=cohort_id,
                    cohortname=request.json["cohortname"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(cohort)
            db.session.commit()

            return generateResponse("Cohort created")
        if (request.method == 'DELETE'):
            cohort = Cohort.query.filter_by(id=cohort_id).first()
            if (cohort):
                db.session.delete(cohort)
                db.session.commit()

                return generateResponse("Cohort deleted")
            else:
                return generateError(404, "Cohort not found")
    except:
        return generateError(500, "Could not process request")