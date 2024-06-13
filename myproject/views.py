from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from destinations.models import Destination
import requests

@api_view(['POST'])
def incoming_data(request):
    app_secret_token = request.headers.get('CL-XTOKEN')
    if not app_secret_token:
        return Response({'error': 'CL-XTOKEN header is missing'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        account = Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        return Response({'error': 'Invalid CL-XTOKEN'}, status=status.HTTP_401_UNAUTHORIZED)
    
    data = request.data
    destinations = Destination.objects.filter(account=account)

    for destination in destinations:
        headers = destination.headers
        url = destination.url
        method = destination.http_method
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=data)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            
            response.raise_for_status()
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({'status': 'success'}, status=status.HTTP_200_OK)

