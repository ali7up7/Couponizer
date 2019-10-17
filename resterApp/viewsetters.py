from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ResterSerializer, CouponerClientSerializer
from .modeler import ResterModel, CouponerClientModel, CouponerClientModelManager

class ResterViewset(viewsets.ModelViewSet):
    serializer_class = ResterSerializer
    queryset = ResterModel.objects.all()


class CouponerClientViewset(viewsets.ModelViewSet):
    serializer_class = CouponerClientSerializer
    queryset = CouponerClientModel.objects.all()





    
