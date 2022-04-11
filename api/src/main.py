# Import libraries
import flask
from models.models import db
import os
from dotenv import load_dotenv


# Import routes
from affinity.affinity import affinity_blueprint
from auth.auth import auth_blueprint
from cohort.cohort import cohort_blueprint
from confirmation.confirmation import confirmation_blueprint
from group.group import group_blueprint
from groupmember.groupmember import groupmember_blueprint
from like.like import like_blueprint
from link.link import link_blueprint
from liveliness.liveliness import liveliness_blueprint
from module.module import module_blueprint
from modulemember.modulemember import modulemember_blueprint
from project.project import project_blueprint
from user.user import user_blueprint


# Load env variables
load_dotenv()
DB_URL = os.getenv('DB_URL')
DB_DBNAME = os.getenv('DB_DBNAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')


app = flask.Flask(__name__)


@app.before_first_request
def create_tables():
    db.create_all()


# Define routes
@app.route('/', methods=['GET'])
def home():
    return {
        "message": "Currently supported endpoints",
        "endpoints": ["/affinity", "/auth", "/cohort", "/confirmation", "/group", "/groupmember", "/like", "/link", "/liveliness", "/module", "/modulemember", "/project", "/user"]
    }


app.register_blueprint(affinity_blueprint, url_prefix="/affinity")
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(cohort_blueprint, url_prefix='/cohort')
app.register_blueprint(confirmation_blueprint, url_prefix='/confirmation')
app.register_blueprint(group_blueprint, url_prefix="/group")
app.register_blueprint(groupmember_blueprint, url_prefix="/groupmember")
app.register_blueprint(like_blueprint, url_prefix="/like")
app.register_blueprint(link_blueprint, url_prefix='/link')
app.register_blueprint(liveliness_blueprint, url_prefix='/liveliness')
app.register_blueprint(module_blueprint, url_prefix="/module")
app.register_blueprint(modulemember_blueprint, url_prefix="/modulemember")
app.register_blueprint(project_blueprint, url_prefix='/project')
app.register_blueprint(user_blueprint, url_prefix='/user')


app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + DB_USER+':'+DB_PASS+'@'+DB_URL+'/'+DB_DBNAME  # nopep8
db.init_app(app)


if __name__ == "__main__":
    # Set up app variables for development
    # The production entrypoint for the project is the wsgi.py file in this directory

    print(app.url_map)
    app.run(port=8000)
    db.create_all()