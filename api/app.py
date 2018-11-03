from api import app, api
from flask_restful import Api
from api.resources.users import SignupStylist,SigninStylist,Signup
from api.resources.hair_stylist import BusinessInfo



api.add_resource(SignupStylist, '/api/v1/auth/signup_stylist')
api.add_resource(Signup,'/api/v1/auth/signin')
api.add_resource(BusinessInfo,'/api/v1/stylist/business')
