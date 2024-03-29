from flask import Flask, request, json, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://UE0kDnSijj:9klWE7urdT@remotemysql.com:3306/UE0kDnSijj'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root_password@localhost:3307/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    age = db.Column(db.Integer)

    def __init__(self, username, password, first_name, last_name, age):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

db.create_all()

class UserSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'age')

user_schema = UserSchema()
users_schema = UserSchema(many=True)




class BaseManager(Resource):
    @staticmethod
    def get(): 
        return Response(response=json.dumps({"Status": "Crude API UP and Running"}),
                    status=200,
                    mimetype='application/json')



class UserManager(Resource):
    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            users = User.query.all()
            return jsonify(users_schema.dump(users))
        user = User.query.get(id)
        return jsonify(user_schema.dump(user))

    @staticmethod
    def post():
        username = request.json['username']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        age = request.json['age']

        user = User(username, password, first_name, last_name, age)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'Message': f'User {first_name} {last_name} successfully inserted.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the user ID' })
        user = User.query.get(id)

        username = request.json['username']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        age = request.json['age']

        user.username = username 
        user.password = password 
        user.first_name = first_name 
        user.last_name = last_name
        user.age = age 

        db.session.commit()
        return jsonify({
            'Message': f'User {first_name} {last_name} succeefully altered.'
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the user ID' })
        user = User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'Message': f'User {str(id)} successfully deleted.'
        })


api.add_resource(BaseManager, '/')
api.add_resource(UserManager, '/api/users')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0")