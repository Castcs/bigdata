from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from services.config import Config, db
from services.routes.api import api
from services.models import *
from services.controllers import *

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize SQLAlchemy and Migrate
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    # UpdateController.upload_salary_data()
    # UpdateController.upload_COL_data()

# Register blueprints
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)
