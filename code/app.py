from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'sebas'
api = Api(app)

jwt = JWT(app, authenticate, identity)

#------ ADDITION OF RESOURCES TO OUR ENDPOINT ------
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
#---------------------------------------------------

if __name__ == '__main__':
    db.init_app(app)
    # We execute/initialize/run our app
    app.run(port=5000, debug=True)  # important to mention debug=True
