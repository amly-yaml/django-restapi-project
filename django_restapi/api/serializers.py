from rest_framework import serializers
from projects.models import Movie

# Create the  - serializers allow complex data such as query set into JSON fromat or others.. etc
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
         # convert all the data table in models file 
        fields = ('moviename', 'description', 'rating', 'image')