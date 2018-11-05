from api import app, api
from flask_restful import Api
from api.resources.users import SignupStylist,SigninStylist,Signup
from api.resources.services import StylistSearch
from api.resources.hair_stylist import BusinessInfo, Hairstyles, OtherServices, SpecificHairStyle



api.add_resource(SignupStylist, '/api/v1/auth/signup_stylist')
api.add_resource(Signup,'/api/v1/auth/signup')
api.add_resource(BusinessInfo,'/api/v1/stylist/business')
api.add_resource(Hairstyles,'/api/v1/stylist/hairstyles')
api.add_resource(OtherServices,'/api/v1/stylist/other_services')
api.add_resource(StylistSearch,'/api/v1/search')
api.add_resource(SpecificHairStyle,'/api/v1/stylist/hairstyle/<int:hairstyleId>')
