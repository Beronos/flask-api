from flask_jwt_extended import create_access_token, create_refresh_token, verify_jwt_in_request, get_jwt
from models import User
from flask_restful import Resource, fields, reqparse
from response import CustomResponse


user_fields = {
    'username': fields.String(attribute='UserName'),
    'password': fields.String(attribute='Password'),
}

reqparse_user = reqparse.RequestParser()
reqparse_user.add_argument('username', type=str, required=True, help='No username provided', location='json')
reqparse_user.add_argument('password', type=str, required=True, help='No pw provided', location='json')


class UserResource(Resource):
    def __init__(self):
        self.reqparse = reqparse_user
        super(UserResource, self).__init__()

    def post(self):
        user_args = self.reqparse.parse_args()
        user = User.get_by_username(user_args['username'])

        if user and User.check_password(user, user_args['password']):
            if user.isAdmin:
                access_token = create_access_token(identity=user.UserName, fresh=True,
                                                   additional_claims={"is_admin": True})
            else:
                access_token = create_access_token(identity=user.UserName, fresh=True,
                                                   additional_claims={"is_admin": False})
            refresh_token = create_refresh_token(identity=user.UserName)

            return CustomResponse.success({'access_token': access_token,
                                           'refresh_token': refresh_token,
                                           'isAdmin': user.isAdmin
                                           }, "Successful authorization!")
        return CustomResponse.error({'msg': 'Invalid credentials'})
