from flask import Flask
from flask_restful import Api
from repository.db import initialize_db
from flask_cors import CORS
from routes import initialize_routes

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/customer-info'
}

initialize_db(app)
initialize_routes(api)

app.run(port=5000, debug=True)
