from rest_framework import serializers
from .modeler import ResterModel,  CouponerClientModel, CouponerClientModelManager

class ResterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResterModel
        fields = ('id', 'meal', 'description')

        

class CouponerClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponerClientModel
        fields = ('id', 'meal', 'coupon')





