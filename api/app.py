from api import app, api
from flask_restful import Api
from api.resources.users import SignupStylist



api.add_resource(SignupStylist, '/api/v1/auth/signup_stylist')