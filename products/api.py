# products/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response

from pixsoft.settings import FIRESTORE_DB as db

class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        products_ref = db.collection("products")
        docs = products_ref.stream()

        products = [doc.to_dict() | {"id": doc.id} for doc in docs]
        return Response(products)

    def retrieve(self, request, pk=None):
        doc = db.collection("products").document(pk).get()
        if not doc.exists:
            return Response({"error": "Not found"}, status=403)

        return Response(doc.to_dict())

    def create(self, request):
        data = request.data
        doc_ref = db.collection("products").add(data)
        return Response({"id": doc_ref[0].id, **data}, status=201)

    def update(self, request, pk=None):
        data = request.data
        db.collection("products").document(pk).set(data, merge=True)
        return Response(data)

    def destroy(self, request, pk=None):
        db.collection("products").document(pk).delete()
        return Response(status=203)
