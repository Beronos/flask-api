from flask_restful import Resource, fields, marshal, reqparse
from response import CustomResponse
from controllers import loan_controller
from admin_required import admin_required


user_fields = {
    'username': fields.String(attribute='UserName'),
}


book_fields = {
    'id': fields.Integer(attribute='ISBN'),
    'title': fields.String(attribute='Title'),
}

loan_fields = {
    'id': fields.Integer(attribute='loanID'),
    'book': fields.Nested(book_fields, attribute='loaned_book'),
    'user': fields.Nested(user_fields)
}


class LoanList(Resource):
    @admin_required()
    def get(self):
        try:
            loans = loan_controller.get_loans()
            return CustomResponse.success(marshal(loans, loan_fields), "List of authors")
        except Exception as e:
            return CustomResponse.error(e)