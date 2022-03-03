from rest_framework.views import APIView
from rest_framework.response import Response
import requests
# @api_view(['POST'])
# def Tekshir(request):
#     #print(request)

#     return Response({"message": "Hello, world!"})


class Tekshir(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    

    def get(self, request):
        """
        Return a list of all users.
        """
        from suds.client import Client
        url = 'http://127.0.0.1:9090/dsvs/pkcs7/v1?wsdl'
        client = Client(url)
        print(client)
        
        return Response({"message": "Hello, world!"})
    def post(self,request):
        print(request.data)

        return Response({"message": "Hello, world!"})