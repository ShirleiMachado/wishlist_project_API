from rest_framework import serializers
from wishlist_app.models import Client, Product, Fav_Product
#from wishlist_app.validators import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    def validate(self,data):
        return data

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class FavProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fav_Product
        fields = '__all__'