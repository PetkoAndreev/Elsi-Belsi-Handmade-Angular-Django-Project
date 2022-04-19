import os
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, logout
from django.middleware import csrf

from rest_framework import generics as api_views, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from elsi_belsi_handmade.elsi_belsi_auth.authenticate import get_tokens_for_user
from elsi_belsi_handmade.elsi_belsi_auth.serializers import CreateUserSerializer, ProfileSerializer

# Get the user model - default one or rewrite which comes from Django
UserModel = get_user_model()


class RegisterView(api_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


# Get customized login view and set JWT access token to cookie
class LoginView(APIView):
    def post(self, request):
        data = request.data
        response = Response()
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data["access"],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = {"Success": "Login successfully", "data": data}
                return response
            else:
                return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid": "Invalid email or password!!"}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    @staticmethod
    def __perform_logout(request):
        response = Response()
        response.delete_cookie('access_token')
        response.data = {
            'message': 'User logout successfully!'
        }
        logout(request)
        return response

    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)


# class LoginView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('access_token')
#
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')
#
#         try:
#             payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')
#
#         user = UserModel.objects.filter(id=payload['user_id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


class ProfileGetUpdateDeleteView(APIView):
    serializer_class = ProfileSerializer

    # TODO: Add IsAuthenticated
    # Show user profile page
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(UserModel, id=self.kwargs['pk'])
        profile_serializer = ProfileSerializer(user.profile)
        return Response(profile_serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            user = get_object_or_404(UserModel, id=self.kwargs['pk'])
            profile = ProfileSerializer(user.profile).data
            profile_serializer = ProfileSerializer(user.profile, data=request.data)
            default_image_name = 'default_profile_image.jpg'
            # Not the best way to do it, but it works - tried different scenarios, but the appropriate way with "os.path.join(settings.MEDIA_ROOT, str(db_pet.image))" didn't works
            image_path = os.path.abspath(os.path.join(settings.MEDIA_ROOT, profile['profile_image'][len('/media/'):]))
            # Check if the profile picture is not the default one and it's changed with a new one
            if default_image_name not in str(image_path) and request.data['profile_image']:
                os.remove(image_path)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response(profile_serializer.data, status=status.HTTP_200_OK)
            return Response(profile_serializer.errors)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            user = get_object_or_404(UserModel, id=self.kwargs['pk'])
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
