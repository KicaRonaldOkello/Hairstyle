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