from api import app, api
from flask_restful import Api
from api.resources.users import SignupStylist,SigninStylist,Signup



api.add_resource(SignupStylist, '/api/v1/auth/signup_stylist')
api.add_resource(SigninStylist,'/api/v1/auth/signin_stylist')
api.add_resource(Signup,'api/v1/auth/signin')
