
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from projects.models import Movie
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


# Create your views here.
@api_view(['GET'])
def routes(request): 
    routes = [
        {"GET": "api/movie_details"},
        {"POST": "api/users/token"}
    ]
    return Response(routes)

# create and read the movie api 
# make permission with JWT token 
@permission_classes([IsAuthenticated])
class MovieAPIView(generics.ListCreateAPIView):
    # fetch all the movie database models 
    queryset = Movie.objects.all()
    # make json format
    serializer_class = ProjectSerializer

# post and delete the movie api 
@permission_classes([IsAuthenticated])
class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # fetch all the movie database models 
    queryset = Movie.objects.all()
    # make json format
    serializer_class = ProjectSerializer

