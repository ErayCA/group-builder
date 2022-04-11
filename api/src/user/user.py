# Import libraries and define blueprint
from models.models import User, db
from flask import Blueprint, request, make_response
from responses import generateResponse, generateError
user_blueprint = Blueprint('user', __name__)


# Route to get all users
@user_blueprint.route('/', methods=['GET'])
def get_all_users():
    try:
        db_users = User.query.all()
        users = []

        for user in db_users:
            users.append(User.jsonify(user))

        return generateResponse(users)
    except:
        return generateError(500, "Could not proccess request")


# Routes to handle single user CRUD actions
@user_blueprint.route('/byID/<user_id>', methods=['GET', 'POST', 'DELETE'])
def manage_user(user_id):
    try:
        if (request.method == 'GET'):
            user = User.query.filter_by(id=user_id).first()

            if (user):
                return generateResponse(User.jsonify(user))
            else:
                return generateError(404, "User not found")
        if (request.method == 'POST'):
            try:
                user = User(
                    id=user_id,
                    firstname=request.json["firstname"],
                    surname=request.json["surname"],
                    email=request.json["email"],
                    password=request.json["password"],
                    registered=False,
                    cohortID=request.json["cohortID"]
                )
            except:
                return generateError(400, "Missing mandatory request paramaters in request body")

            db.session.add(user)
            db.session.commit()

            return generateResponse("User created")
        if (request.method == 'DELETE'):
            user = User.query.filter_by(id=user_id).first()
            if (user):
                db.session.delete(user)
                db.session.commit()

                return generateResponse("User deleted")
            else:
                return generateError(404, "User not found")
    except:
        return generateError(500, "Could not proccess request")


# Route to handle searching users
@user_blueprint.route('/search', methods=['POST'])
def search_users():
    try:
        page = 0
        pageSize = 50
        # Try to read optional paramaters in request
        try:
            page = request.json["page"]
        except:
            pass
        try:
            pageSize = request.json["pageSize"]
        except:
            pass

        # Try to read mandatory paramater in request
        try:
            queries = request.json["queries"]
        except:
            return generateError(400, "Request has to include `queries` array in body")

        # Check and perform queries
        results = []
        for query in queries:
            if (("field" in query) and ("query" in query)):
                field = query["field"]
                value = query["query"]
                try:
                    result = performUserQuery(field, value)
                except:
                    return generateError(500, "Problem processing request query")

                results = addWithoutDuplicating(results, result)

            else:
                return generateError(400, "Badly formated query")

        # Paginate results
        paged_results = list(paginateArray(results, pageSize))

        # Format response
        data = {
            "page": page,
            "pageSize": pageSize,
            "nextPage": (page < (len(paged_results)-1)),
            "results": paged_results[page] if ((page < len(paged_results))) else []
        }

        return generateResponse(data)
    except:
        return generateError(500, "Could not proccess request")


# Helper function to perform and format the actual queries
def performUserQuery(field, value):
    users = []
    if (field == "firstname"):
        users = User.query.filter(User.firstname.contains(value)).order_by(User.id).all()  # nopep8
    if (field == "surname"):
        users = User.query.filter(User.surname.contains(value)).order_by(User.id).all()  # nopep8
    if (field == "cohortID"):
        users = User.query.filter(User.cohortID.contains(value)).order_by(User.id).all()  # nopep8
    if (field == "email"):
        users = User.query.filter(User.email.contains(value)).order_by(User.id).all()  # nopep8
    if (field == "registered"):
        users = User.query.filter(User.registered.contains(value)).order_by(User.id).all()  # nopep8

    results = []
    for user in users:
        results.append(User.jsonify(user))

    return results


# Helper function to append items to an array without duplicating items
def addWithoutDuplicating(arr1, arr2):
    # Check if item is present in arr1, and if not add it
    for itemToAdd in arr2:
        shouldAdd = True
        for itemToCheck in arr1:
            if itemToAdd['id'] == itemToCheck['id']:
                shouldAdd = False
        if (shouldAdd):
            arr1.append(itemToAdd)
    return arr1


# Helper function to paginate results array
def paginateArray(array, pageSize):
    for i in range(0, len(array), pageSize):
        yield array[i:i + pageSize]