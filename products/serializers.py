from rest_framework import serializers
from .models import Product
from .models import Category
from .models import SubCategory



class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    price = serializers.FloatField()
    stock = serializers.IntegerField()
    subcategory = serializers.CharField()
    supplier = serializers.CharField()
    
    rental_enabled = serializers.BooleanField(default=False)
    rental_monthly_price = serializers.FloatField(default=0)
    rental_min_months = serializers.IntegerField(default=0)
    rental_status = serializers.CharField(default="available")
    rented_to = serializers.CharField(allow_null=True, required=False)
    rental_end_date = serializers.DateTimeField(allow_null=True, required=False)


class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()

class SubCategorySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    from_category = serializers.CharField()
    #from_category = CategorySerializer()  # Relación con Category
