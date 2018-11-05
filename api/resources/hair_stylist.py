from api import app
from flask_restful import Resource
from flask import Flask, request, json
from api.dbtask import Business, HairStyle

a = Business()
b = HairStyle()

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

class Hairstyles(Resource):
    def post(self):
        hairstyles = {
            'hairstyle_name':request.json['hairstyle_name'],
            'hairstyle_description':request.json['hairstyle_description'],
            'price_range':request.json['price_range'],
            'staff_id':request.json['staff_id']
        }
        b.add_hairstyle(hairstyles)
        return {"message":"Hairstyle added"}, 201

    def get(self):
        all_hairs = b.get_hairstyles()
        return {"hairstyles": all_hairs}, 200

class SpecificHairStyle(Resource):
    def put(self, hairstyleId):
        hairstyle = {
            'hairstyle_name':request.json['hairstyle_name'],
            'hairstyle_description':request.json['hairstyle_description'],
            'price_range':request.json['price_range'],
            'staff_id':request.json['staff_id']
        }
        b.update_hairstyle(hairstyleId, hairstyle)
        return {"message":"Hairstyle updated"}, 201

    def get(self, hairstyleId):
        specific_hairstyle =  b.get_specific_hairstyle(hairstyleId)
        return {"message":specific_hairstyle}, 200

class OtherServices(Resource):
    def post(self):
        service = {
            'service_name':request.json['service_name'],
            'service_description':request.json['service_description'],
            'price_range':request.json['price_range'],
            'staff_id':request.json['staff_id']
        }
        b.add_services(service)
        return {
            "message":"Service added"
        }, 201
