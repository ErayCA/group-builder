from main import app
from models.models import db


if __name__ == "__main__":
    # Set up app variables for production
    app.config["DEBUG"] = False

    app.run(port=8080)
    db.create_all()