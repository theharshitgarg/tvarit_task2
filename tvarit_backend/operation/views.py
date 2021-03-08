from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_500_INTERNAL_SERVER_ERROR,)

from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError as RestValidationError

from .helpers import view_helpers
from .services.addition import AdditionService


class AdditionView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        response = view_helpers.APIViewErrorResponse()
        result = None
        http_status = HTTP_400_BAD_REQUEST

        try:
            service = AdditionService()
            result = service.result(request.data)

            response = view_helpers.APIViewSuccessResponse()
            response.data = {"result": result}
            http_status = HTTP_200_OK

        except RestValidationError as err:
            response.message = "Invalid request data"

        return Response(response.json(), status=http_status)
