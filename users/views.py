from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status



from .serializers import UserSerializer

@api_view(['POST'])
def register(request):
    
    serializer = UserSerializer(data=request.data)

    #Guarda los datos del usuario en el model User
    if serializer.is_valid():
        serializer.save()

        #Obtiene el usuario que se acaba de registrar
        user = User.objects.get(username=serializer.data['username'])
        #Hashea la contraseña para que el usuario sirva 
        user.set_password(serializer.data['password'])
        #Guarda el usuario
        user.save()

        #Crea el token en base al usuario
        token = Token.objects.create(user=user)
        #Retorna el token.key osea el string
        return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)