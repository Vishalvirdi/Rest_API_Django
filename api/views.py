from rest_framework import generics
from .models import Api
from .serilizer import ApiSerializer
class Create(generics.ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

class ReadUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer