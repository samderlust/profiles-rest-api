from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """REturns a list of Apiview features"""
        an_apiview = [
            'Uses HT TP methods as function',
            'simliar to traditional Django view',
            'control over logic'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """updating object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Partiel update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Partiel update of an object"""
        return Response({'method': 'Delete'})
        

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message"""
        a_viewset=[
            'uses action (list, create , retrieve , update, partiale_update)'
            'automatically maps to urls using routers'
        ]

        return Response({'message': 'hello', 'viewset':a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Handle geting an object by ID"""
        return Response({'method': 'GET'})
    
    def update(self, request, pk=None):
        """updating"""
        return Response({'method':"Put"})

    def partial_update(self, request, pk=None):
        """partial_update"""
        return Response({'method':"patch"})
        
    def destroy(self, request, pk=None):
        """destroy"""
        return Response({'method':"delete"})
        

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle create and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
