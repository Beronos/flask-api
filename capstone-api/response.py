class CustomResponse():
    @staticmethod
    def success(data, msg="Success"):
        response = {
            'success': True,
            'message': msg,
            'body': data,
            'status': 200
        }
        return response

    @staticmethod
    def error(msg=""):
        response = {
            'success': False,
            'description': "Something went wrong! Error: " + str(msg),
            'statuscode': 500
        }
        return response