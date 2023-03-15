from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room

# function based views a view to show us all th routes in our API
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]

    return Response(routes) 

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    return Response(rooms)
# safe allows more than python dictionary to be used inside this response