from flask_restful import Resource, fields, marshal, reqparse
from response import CustomResponse
from controllers import author_controller
from flask_jwt_extended import jwt_required
from admin_required import admin_required

author_fields = {
    'id': fields.Integer(attribute='authorID'),
    'firstName': fields.String(attribute='FirstName'),
    'lastName': fields.String(attribute='LastName'),
}

reqparse_author = reqparse.RequestParser()
reqparse_author.add_argument('firstName', type=str, required=True, help='No first name provided', location='json')
reqparse_author.add_argument('lastName', type=str, required=True, help='No last name provided', location='json')


class AuthorListResource(Resource):
    def __init__(self):
        self.reqparse = reqparse_author
        super(AuthorListResource, self).__init__()

    @jwt_required()
    def get(self):
        try:
            authors = author_controller.get_authors()
            return CustomResponse.success(marshal(authors, author_fields), "List of authors")
        except Exception as e:
            return CustomResponse.error(e)

    @admin_required()
    def post(self):
        try:
            author = self.reqparse.parse_args()
            author_controller.create_author(author['firstName'], author['lastName'])
            return CustomResponse.success(author, "Successfully created!")
        except Exception as e:
            return CustomResponse.error(e)


class AuthorResource(Resource):
    def __init__(self):
        self.reqparse = reqparse_author
        super(AuthorResource, self).__init__()

    @jwt_required()
    def get(self, id):
        try:
            return CustomResponse.success(marshal(author_controller.get_author(id), author_fields))
        except Exception as e:
            return CustomResponse.error(e)

    @admin_required()
    def delete(self, id):
        try:
            return CustomResponse.success(marshal(author_controller.delete_author(id), author_fields),
                                          "Successfully deleted author!")
        except Exception as e:
            return CustomResponse.error(e)

    @admin_required()
    def put(self, id):
        try:
            author = self.reqparse.parse_args()
            return CustomResponse.success(marshal(author_controller.update_author(id, author['firstName'], author['lastName']), author_fields),
                                          "Successfully updated author!")
        except Exception as e:
            return CustomResponse.error(e)



