from api import app
from flask_restful import Resource
from flask import Flask, request, json
from api.dbtask import Users
from flask_restful import reqparse

b = Users()


class SignupStylist(Resource):
    def post(self):
        signup = {
            "firstname": request.json["firstname"],
            "lastname": request.json["lastname"],
            "email": request.json["email"],
            "password": request.json["password"]
        }

        parser = reqparse.RequestParser()
        parser.add_argument('firstname', type=int, help='Please input correct firstname')
        args = parser.parse_args()
        b.signup_users(signup)
        return {"message":"Signup created"}, 201
