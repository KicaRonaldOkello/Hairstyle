import psycopg2
from psycopg2.extras import RealDictCursor
from api import app, api
import os
from config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(os.environ["DATABASE_URL"])
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cur = self.conn.cursor(cursor_factory=RealDictCursor)


    def create_user_table(self):
        users = "CREATE TABLE IF NOT EXISTS users(user_id serial PRIMARY KEY,\
        firstname VARCHAR(50) NOT NULL, lastname VARCHAR(60) NOT NULL,\
        email VARCHAR(60) UNIQUE NOT NULL, password VARCHAR(200) NOT NULL,\
        role VARCHAR(20))"
        self.cur.execute(users)

    def create_business_table(self):
        business = "CREATE TABLE IF NOT EXISTS business(business_id serial PRIMARY KEY,\
        business_name VARCHAR(200) UNIQUE NOT NULL, business_location VARCHAR(60) NOT NULL,\
        business_telephone VARCHAR(30) NOT NULL, staff_id INT, FOREIGN KEY(staff_id) REFERENCES users(user_id) ON DELETE CASCADE)"
        self.cur.execute(business)

    def create_hairstyle_table(self):
        hair = "CREATE TABLE IF NOT EXISTS hairstyle(hairstyle_id serial PRIMARY KEY,\
        hairstyle_name VARCHAR(50) NOT NULL, hairstyle_description VARCHAR(300), price_range VARCHAR(20) NOT NULL,\
        staff_id INT, FOREIGN KEY (staff_id) REFERENCES users(user_id))"
        self.cur.execute(hair)

    def create_services_table(self):
        service = "CREATE TABLE IF NOT EXISTS services(service_id serial PRIMARY KEY,\
        service_name VARCHAR(50) NOT NULL, service_description VARCHAR(300), price_range VARCHAR(20) NOT NULL,\
        staff_id INT, FOREIGN KEY (staff_id) REFERENCES users(user_id) ON DELETE CASCADE)"
        self.cur.execute(service)
