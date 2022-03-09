from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=int,
                        required=True,
                        help="Every store needs a name!"
                        )

    #@jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'Message': 'Store not found'}, 404

    #@jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred creating the store.'}, 500 # Internal Server Error

        return store.json(), 201

    #@jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}

    #@jwt_required()
    def put(self, name):
        store = StoreModel.find_by_name(name)

        if store is None:
            store = StoreModel(name)
        else:
            store.name = name

        store.save_to_db()
        return store.json()


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}