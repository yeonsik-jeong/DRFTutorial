from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from authentication.serializers import LoginSerializer, SignupSerializer

# Create your views here.
class Signup(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=request.data['username'], email=request.data['email'], password=request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            resp = {'username': user.username, 'token': token.key}
            return Response(resp, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        # if serializer.is_valid():
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            resp = {'username': user.username, 'token': token.key}
            return Response(resp, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)