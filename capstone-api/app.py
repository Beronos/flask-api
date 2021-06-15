from datetime import timedelta
from flask import Flask
from flask_restful import Api

from extensions import db
from resources.author_resource import AuthorListResource, AuthorResource
from resources.book_resource import BookListResource, BookResource
from resources.user_resource import UserResource
from resources.loan_resource import LoanList
from flask_jwt_extended import JWTManager

app = Flask(__name__)
db.init_app(app)
api = Api(app)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/capstone_bookstore'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)

# routes
api.add_resource(AuthorListResource, '/authors', )
api.add_resource(AuthorResource, '/authors/<string:id>', )
api.add_resource(BookListResource, '/books')
api.add_resource(BookResource, '/books/<string:id>')
api.add_resource(UserResource, '/login')
api.add_resource(LoanList, '/loans')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
