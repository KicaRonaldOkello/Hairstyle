from api import app, api
from api.models import Database


class Users(Database):
    def signup_users(self, data):
        query = "INSERT INTO users(firstname, lastname, email, password, role)\
        VALUES('{}','{}','{}','{}','{}')".format(data["firstname"], data["lastname"],\
        data["email"], data["password"],data["role"])
        self.cur.execute(query)
        return data

    def check_login(self,data):
        return True

class Business(Database):
    def add_business(self, business):
        query = "INSERT INTO business(business_name, business_location, business_telephone, staff_id)\
        VALUES('{}','{}','{}','{}')".format(business['business_name'], business["business_location"],\
        business["business_telephone"], business["staff_id"])
        self.cur.execute(query)
        return business

class HairStyle(Database):
    def add_hairstyle(self, hair):
        query = "INSERT INTO hairstyle(hairstyle_name, hairstyle_description, price_range, staff_id)\
        VALUES('{}','{}','{}','{}')".format(hair['hairstyle_name'], hair['hairstyle_description'],\
        hair['price_range'], hair['staff_id'])
        self.cur.execute(query)
        return hair

    def get_hairstyles(self):
        query = "SELECT * FROM hairstyle"
        self.dict_cur.execute(query)
        all_hairstyles = self.dict_cur.fetchall()
        return all_hairstyles

    def add_services(self, service):
        query = "INSERT INTO services(service_name, service_description, price_range, staff_id)\
        VALUES('{}','{}','{}','{}')".format(service['service_name'], service['service_description'],\
        service['price_range'], service['staff_id'])
        self.cur.execute(query)
        return service

    def get_specific_hairstyle(self, hairstyleId):
        query = "SELECT * FROM hairstyle WHERE hairstyle_id = '{}'".format(hairstyleId)
        self.cur.execute(query)
        hairstyle = self.cur.fetchone()
        return hairstyle

    def update_hairstyle(self,hairstyleId, hairstyle):
        query = "UPDATE hairstyle SET hairstyle_name = '{}',hairstyle_description = '{}',\
        price_range = '{}', staff_id = '{}' WHERE hairstyle.hairstyle_id = '{}'".format(hairstyle["hairstyle_name"],\
        hairstyle["hairstyle_description"], hairstyle["price_range"], hairstyle["staff_id"],hairstyleId)
        self.cur.execute(query)
        return hairstyle