from api import app
from flask_restful import Resource
from flask import Flask, request, json
from api.dbtask import Users
from flask_restful import reqparse

b = Users()


class SignupStylist(Resource):
    role="sylist"
    def post(self):
        signup = {
            "firstname": request.json.get("firstname",None),
            "lastname": request.json.get("lastname",None),
            "email": request.json.get("email",None),
            "password": request.json.get("password",None),
            "role":self.role
        }
        parser = reqparse.RequestParser()
        parser.add_argument('firstname', type=int, help='Please input correct firstname',required=True)
        args = parser.parse_args()
        b.signup_users(signup)
        return {"message":"Signup created"}, 201

class SigninStylist(Resource):
    def post(self):
        user={
            "email":request.json.get("email",None),
            "password":request.json.get("password",None)
        }
        if user['email'] is None or user['password'] is None:
            return {"message":"missing parameter"}
        if b.check_login(user):
            return {"message":"","token":""}
        return {"message":"invalid user credentials"}

class Signup(SignupStylist):
    role="user"


