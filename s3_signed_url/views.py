from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from helper.functions import create_presigned_url


# Create your views here.

class GetPreSignedUrl(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    http_method_names = ['post']

    def post(self, request, fromat=None):
        response = create_presigned_url(
            request.data['fileName'], request.data['fileType'])
        return Response(status=HTTP_200_OK, data={
            'success': True,
            'message': 'signed url obtained',
            'data': [response]
        })
