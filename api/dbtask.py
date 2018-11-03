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