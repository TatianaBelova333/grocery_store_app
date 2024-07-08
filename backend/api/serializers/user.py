from django.contrib.auth import get_user_model
from django.db import DatabaseError, transaction
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from users.models import ShoppingCart

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    """
    Serializer for registering a new user.

    """

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'id',
        ]
        read_only_fields = ('id',)

    def create(self, validated_data):
        '''
        Hash the new user's password before saving
        and create a shopping cart for the new user.
        '''

        try:
            with transaction.atomic():
                user = User.objects.create(**validated_data)
                user.set_password(validated_data["password"])
                user.save()
                ShoppingCart.objects.create(user=user)
        except DatabaseError:
            raise serializers.ValidationError(
                'Во время регистрации произошла ошибка.'
            )

        return user
