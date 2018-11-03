from api.app import app, api
from api.models import Database

a = Database()
a.create_user_table()
a.create_business_table()
a.create_hairstyle_table()


if __name__ == '__main__':
    app.run(debug=True)