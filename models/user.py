from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password): # def __init__(self, _id, username, password):
        # _id is not needed here (constructor) since the attribute _id is a
        # PK given by SQLAlchemy and auto-increments each time we make an insertion to the DB.
        # The request does not take the id as a parameter and therefore is not important
        # to the object creation process
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username1):
        return cls.query.filter_by(username=username1).first()  # SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()  # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()