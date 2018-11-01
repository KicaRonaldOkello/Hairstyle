from api import app, api
from api.models import Database


class Users(Database):
    def signup_users(self, data):
        query = "INSERT INTO users(firstname, lastname, email, password, role)\
        VALUES('{}','{}','{}','{}','stylist')".format(data["firstname"], data["lastname"],\
        data["email"], data["password"])
        self.cur.execute(query)
        return data
