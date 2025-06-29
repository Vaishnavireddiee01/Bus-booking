from django.shortcuts import render

# Create your views here.

# logic for authentication, permission,token, status, response, generics, apiviews

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, BusSerializer
from .models import Bus

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username, password=password)

        if user:
            token, created=Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id 
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class BusListCreateView(generics.ListCreateAPIView):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer
class BusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer
    permission_classes=[IsAuthenticated]

#    def get_permissions(self):
 #       if self.request.method in ['PUT', 'PATCH', 'DELETE']:
  #          return [IsAuthenticated()]
   #     return super().get_permissions()
