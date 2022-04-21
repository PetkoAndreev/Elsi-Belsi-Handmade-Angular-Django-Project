from django.contrib.auth import get_user_model
from rest_framework import serializers
from elsi_belsi_handmade.elsi_belsi_auth.models import Profile

# Get the user model - default one or rewrited which comes from Django
from elsi_belsi_handmade.elsi_belsi_products.serializers import ProductsListSerializer

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            UserModel.USERNAME_FIELD,
            'password',
            'confirm_password',
        )

    # Fix the issue with password as plain text in the db table user
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.confirm_password = ''
        user.save()
        return user

    # Called on return to hide the password from response
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        result.pop('confirm_password')
        return result

    # Overwrite method validate - to be able to use Django password validators from settings.py
    def validate(self, data):
        if not data.get(UserModel.USERNAME_FIELD):
            raise serializers.ValidationError('Please enter a email address.')
        if UserModel.objects.filter(email=UserModel.USERNAME_FIELD).first():
            raise serializers.ValidationError('Someone with that email address has already registered. Was it you?')
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError('Please enter a password and confirm it.')
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError('Those passwords don\'t match.')
        return data


class UserSerializer(serializers.ModelSerializer):
    products = ProductsListSerializer(many=True)

    class Meta:
        model = UserModel
        fields = ['email', 'date_joined', 'products', ]


class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = ('user_id', 'first_name', 'last_name', 'age', 'profile_image',
                  'facebook_url', 'linked_in_url', 'github_url',
                  )
        # depth = 2

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.partial_update(request, *args, **kwargs)
