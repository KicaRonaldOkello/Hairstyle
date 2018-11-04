from flask_restful import Resource
from flask import request
from api.dbtask import HairStyle
import json

hair = HairStyle()


class StylistSearch(Resource):
    def get(get):
        search=request.args
        try:
            response = hair.get_stylists(search)
            return response
        except:
            return {'error':'invalid search parameter'},400


