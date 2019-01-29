from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidVerificationException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid verification'
    default_code = 'invalid_verification'


class AlreadyVerifiedException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Already verified'
    default_code = 'already_verified'


class ExceedLimitException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Exceed limit'
    default_code = 'exceed_limit'
