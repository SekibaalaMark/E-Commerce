from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationView(APIView):
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                "id": user.id,
                "username": user.username,
                "role": user.role,
                "email": user.email
            }
            return Response(response_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self,request):
        serializer = loginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Login succesful",
            "user":{
                "id": user.id,
                "username": user.username,
                "role": user.role,
                "email": user.email

            },
            "tokens":{
                "refresh":str(refresh),
                "access":str(refresh.token)
            }
        },status=status.HTTP_200_OK)