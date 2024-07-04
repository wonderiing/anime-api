from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class BaseViewSet(viewsets.ModelViewSet):
    serializer_class = None

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk != None:
            return model.object.filter(id=pk, is_active = True)
        return model.objects.all()
    
    def destroy(self, request,pk=None):
        object = self.get_queryset().filter(id=pk).first()

        if object:
            object.is_active = False
            object.save()
            return Response({"mensaje": "Objeto eliminado correctamente"}, status=status.HTTP_200_OK)
        return Response({"error": "no encontrado"}, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [IsAuthenticated]
