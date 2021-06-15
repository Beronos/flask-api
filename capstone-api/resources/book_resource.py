from flask_restful import Resource, fields, marshal, reqparse
from response import CustomResponse
from controllers import book_controller
from flask_jwt_extended import jwt_required
from admin_required import admin_required

author_fields = {
    'id': fields.Integer(attribute='authorID'),
    'firstName': fields.String(attribute='FirstName'),
    'lastName': fields.String(attribute='LastName'),
}

book_fields = {
    'id': fields.Integer(attribute='ISBN'),
    'title': fields.String(attribute='Title'),
    'publicationYear': fields.Integer(attribute='PublicationYear'),
    'stock': fields.Integer(attribute='Stock'),
    'rating': fields.Float(attribute='Rating'),
    'description': fields.String(attribute='Description'),
    'genre': fields.String(attribute='Genre'),
    'IMGLocation': fields.String(attribute='IMGLocation'),
    'authors': fields.Nested(author_fields),
}

reqparse_book = reqparse.RequestParser()
reqparse_book.add_argument('title', type=str, required=True, help='No title provided', location='json')
reqparse_book.add_argument('publicationYear', type=int, required=True, help='No publicationYear provided',
                                location='json')
reqparse_book.add_argument('stock', type=int, required=True, help='No stock provided', location='json')
reqparse_book.add_argument('rating', type=float, required=True, help='No rating provided', location='json')
reqparse_book.add_argument('description', type=str, required=True, help='No description provided',
                                location='json')
reqparse_book.add_argument('genre', type=str, required=True, help='No genre provided', location='json')
reqparse_book.add_argument('IMGLocation', type=str, help='No IMGLocation provided',
                                location='json')
reqparse_book.add_argument('authors_id', type=list, required=True, help='No authors provided',
                                location='json')

class BookListResource(Resource):
    def __init__(self):
        self.reqparse = reqparse_book
        super(BookListResource, self).__init__()

    @jwt_required()
    def get(self):
        try:
            return CustomResponse.success(marshal(book_controller.get_books(), book_fields), "List of books")
        except Exception as e:
            return CustomResponse.error(e)

    @admin_required()
    def post(self):
        try:
            return CustomResponse.success(marshal(book_controller.create_book(self.reqparse.parse_args()), book_fields),
                                          "Successfully created book!")
        except Exception as e:
            return CustomResponse.error(e)


class BookResource(Resource):
    def __init__(self):
        self.reqparse = reqparse_book
        super(BookResource, self).__init__()

    @jwt_required()
    def get(self, id):
        try:
            return CustomResponse.success(marshal(book_controller.get_book(id), book_fields))
        except Exception as e:
            return CustomResponse.error(e)

    @admin_required()
    def delete(self, id):
        try:
            return CustomResponse.success(marshal(book_controller.delete_book(id), book_fields),
                                          "Successfully deleted book!")
        except Exception as e:
            return CustomResponse.error(e)

    @admin_required()
    def put(self, id):
        try:
            return CustomResponse.success(marshal(book_controller.update_book(id, reqparse_book.parse_args()),
                                                  book_fields),
                                          "Successfully updated book!")
        except Exception as e:
            return CustomResponse.error(e)
