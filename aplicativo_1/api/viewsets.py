from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from aplicativo_1.models import Person
from .serializers import PersonSerializer

class PersonViewSet(ModelViewSet):
    
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
