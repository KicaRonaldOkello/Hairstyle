import psycopg2
from psycopg2.extras import RealDictCursor
from api import app, api


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="hairstyle",user="postgres",host="localhost",password="password")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cur = self.conn.cursor(cursor_factory=RealDictCursor)

        print("Connected to database")

    def create_user_table(self):
        users = "CREATE TABLE IF NOT EXISTS users(user_id serial PRIMARY KEY,\
        firstname VARCHAR(50) NOT NULL, lastname VARCHAR(60) UNIQUE NOT NULL,\
        email VARCHAR(60) UNIQUE NOT NULL, password VARCHAR(200) NOT NULL,\
        role VARCHAR(20))"
        self.cur.execute(users)
    def create_business_table(self):
        business = "CREATE TABLE IF NOT EXISTS business(business_id serial PRIMARY KEY,\
        business_name VARCHAR(200) UNIQUE NOT NULL, business_location VARCHAR(60) NOT NULL,\
        business_telephone VARCHAR(30) NOT NULL, staff_id INT, FOREIGN KEY(staff_id) REFERENCES users(user_id))"
        self.cur.execute(business)