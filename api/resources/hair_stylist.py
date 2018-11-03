from api import app
from flask_restful import Resource
from flask import Flask, request, json
from api.dbtask import Business

a = Business()

class BusinessInfo(Resource):
    def post(self):
        business_info = {
            'business_name': request.json['business_name'],
            'business_location':request.json['business_location'],
            'business_telephone':request.json['business_telephone'],
            'staff_id':request.json['staff_id']
        }
        a.add_business(business_info)
        return {"message":"Business info added"}, 201