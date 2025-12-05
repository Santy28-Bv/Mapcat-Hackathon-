from rest_framework import serializers
from .models import Product
from .models import Category
from .models import SubCategory
from pixsoft.settings import FIRESTORE_DB as db



#class ProductSerializer(serializers.Serializer):
    #id = serializers.CharField(read_only=True)
    #name = serializers.CharField()
    #price = serializers.FloatField()
    #stock = serializers.IntegerField()
    #subcategory = serializers.CharField()
    #supplier = serializers.CharField()
    #
    #rental_enabled = serializers.BooleanField(default=False)
    #rental_monthly_price = serializers.FloatField(default=0)
    #rental_min_months = serializers.IntegerField(default=0)
    #rental_status = serializers.CharField(default="available")
    #rented_to = serializers.CharField(allow_null=True, required=False)
    #rental_end_date = serializers.DateTimeField(allow_null=True, required=False)

class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    sku = serializers.CharField()
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

    def validate_sku(self, value):
        sku_lower = value.strip().lower()
        product_id = getattr(self.instance, "id", None)

        # Buscar productos existentes con el mismo SKU
        existing = db.collection("products").where("sku_lower", "==", sku_lower).stream()
        for doc in existing:
            if product_id is None or doc.id != product_id:
                raise serializers.ValidationError("SKU already exists")

        return value


    def validate_subcategory(self, value):
        docs = db.collection("subcategories").where("name", "==", value).stream()
        docs_list = list(docs)
        if not docs_list:
            raise serializers.ValidationError("Subcategory does not exist")
    
        return docs_list[0].id


    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        ret["sku_lower"] = ret["sku"].strip().lower()
        return ret

class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    
    def validate_name(self, value):
        name_lower = value.strip().lower()
        category_id = getattr(self.instance, "id", None)

        # Buscar categorías existentes con el mismo nombre
        existing = db.collection("categories").where("name_lower", "==", name_lower).stream()
        for doc in existing:
            if category_id is None or doc.id != category_id:
                raise serializers.ValidationError("Category with this name already exists")

        return value

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        ret["name_lower"] = ret["name"].strip().lower()
        return ret


class SubCategorySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(required=False, allow_blank=True)
    from_category = serializers.CharField() 

    def validate_name(self, value):
        name_lower = value.strip().lower()
        category_id = self.initial_data.get("from_category")
        subcategory_id = getattr(self.instance, "id", None)

        if not category_id:
            raise serializers.ValidationError("from_category is required")

        # Buscar subcategorías existentes con el mismo nombre y categoría
        existing = db.collection("subcategories") \
                     .where("name_lower", "==", name_lower) \
                     .where("from_category", "==", category_id) \
                     .stream()

        for doc in existing:
            if subcategory_id is None or doc.id != subcategory_id:
                raise serializers.ValidationError("Subcategory with this name already exists in this category")

        return value

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        ret["name_lower"] = ret["name"].strip().lower()
        return ret