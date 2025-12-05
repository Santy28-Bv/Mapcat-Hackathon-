# users/views.py
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
##### Crud Usuarios
class UserViewSet(viewsets.ViewSet):

    # Devuelve todos los usuarios
    def list(self, request):
        users_ref = db.collection("users")
        docs = users_ref.stream()

        users = [doc.to_dict() | {"id": doc.id} for doc in docs]
        return Response(users)

    # Devuelve usuario por ID (generado en firebase)
    def retrieve(self, request, pk=None):
        doc = db.collection("users").document(pk).get()
        if not doc.exists:
            return Response({"error": "Not found"}, status=403)

        return Response(doc.to_dict() | {"id": doc.id})

    # Crea un usuario
    def create(self, request):
        data = request.data

        # Aquí podrías validar campos obligatorios como email, password, etc.
        result = db.collection("users").add(data)
        ref = extract_ref(result)

        if not ref:
            return Response({"error": "Firestore insert error"}, status=500)

        return Response({**data, "id": ref.id}, status=201)

    # Actualiza un usuario
    def update(self, request, pk=None):
        data = request.data
        db.collection("users").document(pk).set(data, merge=True)
        return Response(data)

    # Elimina un usuario
    def destroy(self, request, pk=None):
        db.collection("users").document(pk).delete()
        return Response(status=203)