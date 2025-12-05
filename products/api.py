# products/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response

from pixsoft.settings import FIRESTORE_DB as db

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

        return Response(doc.to_dict())

    # Crea un productos
    def create(self, request):
        data = request.data
        doc_ref = db.collection("products").add(data)
        return Response({"id": doc_ref[0].id, **data}, status=201)

    # Actualiza un producto(se actualizan solo los que se envian)
    def update(self, request, pk=None):
        data = request.data
        db.collection("products").document(pk).set(data, merge=True)
        return Response(data)

    # Elimina un producto
    def destroy(self, request, pk=None):
        db.collection("products").document(pk).delete()
        return Response(status=203)

###########################################
## Categorias
class CategoryViewSet(viewsets.ViewSet):

    # Devuelve todas las categorias
    def list(self, request):
        categories_ref = db.collection("categories")
        docs = categories_ref.stream()

        categories = [doc.to_dict() | {"id": doc.id} for doc in docs]
        return Response(categories)

    # Devuelve categoria por Id
    def retrieve(self, request, pk=None):
        doc = db.collection("categories").document(pk).get()
        if not doc.exists:
            return Response({"error": "Not found"}, status=403)

        return Response(doc.to_dict())

    # Crea una categoria
    def create(self, request):
        data = request.data
        doc_ref = db.collection("categories").add(data)
        return Response({"id": doc_ref[0].id, **data}, status=201)

    # Actualiza una categoria
    def update(self, request, pk=None):
        data = request.data
        db.collection("categories").document(pk).set(data, merge=True)
        return Response(data)

    # Elimina una categoria
    def destroy(self, request, pk=None):
        db.collection("categories").document(pk).delete()
        return Response(status=203)


# Subcategorias
class SubCategoryViewSet(viewsets.ViewSet):
    # Devuelve todas las Subcategorias
    def list(self, request):
        subcategories_ref = db.collection("subcategories")
        docs = subcategories_ref.stream()

        subcategories = [doc.to_dict() | {"id": doc.id} for doc in docs]
        return Response(subcategories)

    # Devuelve subcategoria por ID (generado en firebase)
    def retrieve(self, request, pk=None):
        doc = db.collection("subcategories").document(pk).get()
        if not doc.exists:
            return Response({"error": "Not found"}, status=403)

        return Response(doc.to_dict())

    # Crea una subcategoria
    def create(self, request):
        data = request.data
        doc_ref = db.collection("subcategories").add(data)
        return Response({"id": doc_ref[0].id, **data}, status=201)

    # Actualiza un subcategoria
    def update(self, request, pk=None):
        data = request.data
        db.collection("subcategories").document(pk).set(data, merge=True)
        return Response(data)

    # Elimina una subcategoria
    def destroy(self, request, pk=None):
        db.collection("subcategories").document(pk).delete()
        return Response(status=203)