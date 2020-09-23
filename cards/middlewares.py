from django.http import HttpResponse

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

class ErrorMiddleware(BaseMiddleware):

    ERRORS = {
        'NOT_FOUND': {
            'code': 404,
            'message': 'There is no card with the id.'
        },
        'BAD_REQUEST': {
            'code': 400,
            'message': 'Invalid request data or no "author" provided.'
        },
        'FORBIDDEN': {
            'code': 403,
            'message': 'You do not have permission to perform this request because you are not the author of this card.'
        },
        'INTERNAL_SERVER_ERROR': {
            'code': 500,
            'message': 'The server has encountered a situation it does not know how to handle.'
        }
    }

    def process_exception(self, request, exception):

        # Get error message code from request header
        error_message = request.META.get('error_message')

        # Raise internal server error in case of no desired error type available.
        if error_message not in self.ERRORS:
            return HttpResponse(self.ERRORS['INTERNAL_SERVER_ERROR']['message'], status=self.ERRORS['INTERNAL_SERVER_ERROR']['code'])
        return HttpResponse(self.ERRORS[error_message]['message'], status=self.ERRORS[error_message]['code'])
