from rest_framework import viewsets, status
from rest_framework.response import Response
from pixsoft.settings import FIRESTORE_DB as db

from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer
from .models import Product, Category, SubCategory
from rest_framework.decorators import action

# Función para extraer DocumentReference sin importar el orden
def extract_ref(result):
    for item in result:
        if hasattr(item, "id"):
            return item
    return None



class ProductViewSet(viewsets.ViewSet):
 # GET /products/
    def list(self, request):
        products_ref = db.collection("products")
        docs = products_ref.stream()
        products = []

        for doc in docs:
            data = doc.to_dict() | {"id": doc.id}
            serializer = ProductSerializer(data)
            products.append(serializer.data)

        return Response(products)

    # GET /products/{id}/
    def retrieve(self, request, pk=None):
        doc = db.collection("products").document(pk).get()
        if not doc.exists:
            return Response({"error": "Not found"}, status=404)

        data = doc.to_dict() | {"id": doc.id}
        serializer = ProductSerializer(data)
        return Response(serializer.data)

    # POST /products/
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # Guardar en Firestore
            result = db.collection("products").add(data)
            ref = extract_ref(result)
            return Response({**data, "id": ref.id}, status=201)
        return Response(serializer.errors, status=201)

    # PUT /products/{id}/
    def update(self, request, pk=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            db.collection("products").document(pk).set(data, merge=True)
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE /products/{id}/
    def destroy(self, request, pk=None):
        db.collection("products").document(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





    ####### utilidades para filtrar y buscar 
   

 # GET /products/by_subcategory/?subcategory=sub1,sub2
    @action(detail=False, methods=["get"])
    def by_subcategory(self, request):
        subcategories = request.query_params.get("subcategory", "")
        subcategory_ids = subcategories.split(",") if subcategories else []

        docs = db.collection("products").stream()
        products = []

        for doc in docs:
            data = doc.to_dict() | {"id": doc.id}
            if subcategory_ids and data.get("subcategory") not in subcategory_ids:
                continue
            serializer = ProductSerializer(data)
            products.append(serializer.data)

        return Response({"count": len(products), "results": products})



class CategoryViewSet(viewsets.ViewSet):
    # GET /categories/
    def list(self, request):
        categories_ref = db.collection("categories")
        docs = categories_ref.stream()
        categories = []

        for doc in docs:
            data = doc.to_dict() | {"id": doc.id}
            serializer = CategorySerializer(data)
            categories.append(serializer.data)
        return Response(categories)

    # GET /categories/
    def retrieve(self, request, pk=None):
        doc = db.collection("categories").document(pk).get()
        if not doc.exists():
            return Response({"error":"Not found"}, status=404)
        data = doc.to_dict() | {"id": doc.id}
        serializer = CategorySerializer(data)
        return Response(serializer.data)
    
    # POST /categories/
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            result = db.collection("categories").add(data)
            ref = extract_ref(result)
            return Response({**data, "id": ref.id}, status=201)
        return Response(serializer.error, status=201)

    # POST /products/
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # Guardar en Firestore
            result = db.collection("categories").add(data)
            ref = extract_ref(result)
            return Response({**data, "id": ref.id}, status=201)
        return Response(serializer.errors, status=201)

    # PUT /products/{id}/
    def update(self, request, pk=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            db.collection("categories").document(pk).set(data, merge=True)
            return Response(data)
        return Response(serializer.errors, status=404)

    # DELETE /products/{id}/
    def destroy(self, request, pk=None):
        db.collection("categories").document(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

    
    
   

class SubCategoryViewSet(viewsets.ViewSet):
    # GET /categories/
    def list(self, request):
        subcategories_ref = db.collection("subcategories")
        docs = subcategories_ref.stream()
        subcategories = []

        for doc in docs:
            data = doc.to_dict() | {"id": doc.id}
            serializer = SubCategorySerializer(data)
            subcategories.append(serializer.data)
        return Response(subcategories)

    # GET /categories/
    def retrieve(self, request, pk=None):
        doc = db.collection("subcategories").document(pk).get()
        if not doc.exists():
            return Response({"error":"Not found"}, status=404)
        data = doc.to_dict() | {"id": doc.id}
        serializer = SubCategorySerializer(data)
        return Response(serializer.data)
    
    # POST /categories/
    def create(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            result = db.collection("subcategories").add(data)
            ref = extract_ref(result)
            return Response({**data, "id": ref.id}, status=201)
        return Response(serializer.error, status=201)

    # POST /products/
    def create(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # Guardar en Firestore
            result = db.collection("subcategories").add(data)
            ref = extract_ref(result)
            return Response({**data, "id": ref.id}, status=201)
        return Response(serializer.errors, status=201)

    # PUT /products/{id}/
    def update(self, request, pk=None):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            db.collection("subcategories").document(pk).set(data, merge=True)
            return Response(data)
        return Response(serializer.errors, status=404)

    # DELETE /products/{id}/
    def destroy(self, request, pk=None):
        db.collection("subcategories").document(pk).delete()
        return Response(status=204)    