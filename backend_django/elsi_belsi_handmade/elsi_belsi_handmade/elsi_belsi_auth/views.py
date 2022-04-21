import os
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, logout
from django.middleware import csrf

from rest_framework import generics as api_views, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from elsi_belsi_handmade.elsi_belsi_auth.models import Profile
from elsi_belsi_handmade.elsi_belsi_auth.serializers import CreateUserSerializer, ProfileSerializer
from elsi_belsi_handmade.elsi_belsi_products.models import Product
from elsi_belsi_handmade.elsi_belsi_products.serializers import ProductsListSerializer
from elsi_belsi_handmade.utils.utils import HasRequiredPermissionForPostPutPatchDelete, get_tokens_for_user, \
    image_update_delete

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
                    value=data['access'],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = {'Success': 'Login successfully', 'data': data}
                return response
            else:
                return Response({'No active': 'This account is not active!'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Invalid': 'Invalid email or password!'}, status=status.HTTP_404_NOT_FOUND)


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


class ProfileGetUpdateDeleteView(APIView):
    # queryset = Profile.objects.all()
    # lookup_url_kwarg = 'pk'
    serializer_class = ProfileSerializer
    permission_classes = [HasRequiredPermissionForPostPutPatchDelete]
    put_permission_required = 'be the owner of the profile'
    patch_permission_required = 'be the owner of the profile'
    delete_permission_required = 'be the owner of the profile'
    put_patch_error_message = {
        'message': 'You are not the owner of this profile and you can\'t perform UPDATE operation on it!'}
    delete_error_message = {
        'message': 'You are not the owner of this profile and you can\'t perform DELETE operation on it!'}

    def get_object(self, pk):
        return get_object_or_404(UserModel, id=pk)

    # Show user profile page
    def get(self, request, *args, **kwargs):
        user = self.get_object(pk=self.kwargs['pk'])
        profile_serializer = ProfileSerializer(user.profile)
        products = Product.objects.filter(prd_user=profile_serializer.data['user_id'])
        favorites = Product.objects.filter(favorites__user_id=profile_serializer.data['user_id'])

        product_serializer = ProductsListSerializer(products, many=True)
        favorites_serializer = ProductsListSerializer(favorites, many=True)

        result = profile_serializer.data
        result['products'] = product_serializer.data
        result['favorites'] = favorites_serializer.data

        return Response(result)

    def put(self, request, *args, **kwargs):
        try:
            user = self.get_object(pk=self.kwargs['pk'])
            if user.id == request.user.id:
                profile = ProfileSerializer(user.profile).data
                profile_serializer = ProfileSerializer(user.profile, data=request.data)
                default_image_name = 'default_profile_image.jpg'
                # Not the best way to do it, but it works - tried different scenarios, but the appropriate way with "os.path.join(settings.MEDIA_ROOT, str(db_pet.image))" didn't works
                image_path = os.path.abspath(
                    os.path.join(settings.MEDIA_ROOT, profile['profile_image'][len('/media/'):]))
                # Check if the profile picture is not the default one and it's changed with a new one
                if default_image_name not in str(image_path) and 'profile_image' in request.data.keys():
                    os.remove(image_path)
                if profile_serializer.is_valid():
                    profile_serializer.save()
                    return Response(profile_serializer.data, status=status.HTTP_200_OK)
                return Response(profile_serializer.errors)
            return Response(self.put_patch_error_message, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(self.put_patch_error_message, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        try:
            user = self.get_object(pk=self.kwargs['pk'])
            if user.id == request.user.id:
                profile = ProfileSerializer(user.profile).data
                profile_serializer = ProfileSerializer(user.profile, data=request.data,
                                                       partial=True)  # set partial=True to update a data partially
                default_image_name = 'default_profile_image.jpg'
                # Not the best way to do it, but it works - tried different scenarios, but the appropriate way with "os.path.join(settings.MEDIA_ROOT, str(db_pet.image))" didn't works
                image_path = os.path.abspath(
                    os.path.join(settings.MEDIA_ROOT, profile['profile_image'][len('/media/'):]))
                # Check if the profile picture is not the default one and it's changed with a new one
                if default_image_name not in str(image_path) and 'profile_image' in request.data.keys():
                    os.remove(image_path)
                if profile_serializer.is_valid():
                    profile_serializer.save()
                    return Response(profile_serializer.data, status=status.HTTP_200_OK)
                return Response(profile_serializer.errors)
            return Response(self.put_patch_error_message, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(self.put_patch_error_message, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            user = self.get_object(pk=self.kwargs['pk'])
            if user.id == request.user.id:
                profile = ProfileSerializer(user.profile).data
                default_image_name = 'default_profile_image.jpg'
                # Not the best way to do it, but it works - tried different scenarios, but the appropriate way with "os.path.join(settings.MEDIA_ROOT, str(db_pet.image))" didn't works
                image_path = os.path.abspath(
                    os.path.join(settings.MEDIA_ROOT, profile['profile_image'][len('/media/'):]))
                # Check if the profile picture is not the default one and it's changed with a new one
                if default_image_name not in str(image_path):
                    os.remove(image_path)
                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(self.delete_error_message, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(self.delete_error_message, status=status.HTTP_404_NOT_FOUND)
