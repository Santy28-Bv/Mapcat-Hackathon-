# products/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response

from pixsoft.settings import FIRESTORE_DB as db


# ——————————————————————————————
# Función para extraer DocumentReference sin importar el orden
def extract_ref(result):
    for item in result:
        if hasattr(item, "id"):
            return item
    return None
# ——————————————————————————————


#############################################
##### Crud Productos
class ProductViewSet(viewsets.ViewSet):

    # Devuelve todos los productos
    def list(self, request):
        products_ref = db.collection("products")
        docs = products_ref.stream()

        products = [doc.to_dict() | {"id": doc.id} for doc in docs]
        return Response(products)

    # Devuelve producto por ID (generado en firebase)
    def retrieve(self, request, pk=None):
        doc = db.collection("products").document(pk).get()
        if not doc.exists:
            return Response({"error": "Not found"}, status=403)

        return Response(doc.to_dict() | {"id": doc.id})

    # Crea un producto
    def create(self, request):
        data = request.data

        result = db.collection("products").add(data)
        ref = extract_ref(result)

        if not ref:
            return Response({"error": "Firestore insert error"}, status=500)

        return Response({**data, "id": ref.id}, status=201)

    # Actualiza un producto
    def update(self, request, pk=None):
        data = request.data
        db.collection("products").document(pk).set(data, merge=True)
        return Response(data)

    # Elimina un producto
    def destroy(self, request, pk=None):
        db.collection("products").document(pk).delete()
        return Response(status=203)


###########################################
## Categorías
class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        categories_ref = db.collection("categories")
        docs = categories_ref.stream()

        categories = [doc.to_dict() | {"id": doc.id} for doc in docs]
        return Response(categories)

    def retrieve(self, request, pk=None):
        doc = db.collection("categories").document(pk).get()
        if not doc.exists:
            return Response({"error": "Not found"}, status=403)

        return Response(doc.to_dict() | {"id": doc.id})

    def create(self, request):
        data = request.data

        result = db.collection("categories").add(data)
        ref = extract_ref(result)

        if not ref:
            return Response({"error": "Firestore insert error"}, status=500)

        return Response({**data, "id": ref.id}, status=201)

    def update(self, request, pk=None):
        data = request.data
        db.collection("categories").document(pk).set(data, merge=True)
        return Response(data)

    def destroy(self, request, pk=None):
        db.collection("categories").document(pk).delete()
        return Response(status=203)


###########################################
## Subcategorías
class SubCategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        subcategories_ref = db.collection("subcategories")
        docs = subcategories_ref.stream()

        subcategories = [doc.to_dict() | {"id": doc.id} for doc in docs]
        return Response(subcategories)

    def retrieve(self, request, pk=None):
        doc = db.collection("subcategories").document(pk).get()
        if not doc.exists:
            return Response({"error": "Not found"}, status=403)

        return Response(doc.to_dict() | {"id": doc.id})

    def create(self, request):
        data = request.data

        result = db.collection("subcategories").add(data)
        ref = extract_ref(result)

        if not ref:
            return Response({"error": "Firestore insert error"}, status=500)

        return Response({**data, "id": ref.id}, status=201)

    def update(self, request, pk=None):
        data = request.data
        db.collection("subcategories").document(pk).set(data, merge=True)
        return Response(data)

    def destroy(self, request, pk=None):
        db.collection("subcategories").document(pk).delete()
        return Response(status=203)
