# Get the user model - default one or rewrited which comes from Django
from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password')

    # Fix the issue with password as plain text in the db table user
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # Called on return to hide the password from response
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result

    # Ovewrite method validate - to be able to use Django password validators from settings.py
    def validate(self, data):
        # invoke validators here
        return super().validate(data)
