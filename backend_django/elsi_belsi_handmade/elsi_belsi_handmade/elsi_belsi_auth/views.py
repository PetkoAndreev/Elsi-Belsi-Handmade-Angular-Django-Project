from django.contrib.auth import get_user_model
from rest_framework import generics as api_views

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from elsi_belsi_handmade.elsi_belsi_auth.serializers import CreateUserSerializer

UserModel = get_user_model()


# Get the user model - default one or rewrited which comes from Django
class RegisterView(api_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = UserModel.objects.filter(email=email).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        return Response({
            'message': 'success'
        })


class LogoutView:
    pass
