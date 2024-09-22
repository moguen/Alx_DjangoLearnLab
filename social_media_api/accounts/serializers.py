from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model
User = get_user_model()
fild=serializers.CharField()
class UserSerializer(serializers.ModelSerializer):
    # Password field should be write-only and required
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'bio', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is not returned in responses
        }

    def create(self, validated_data):
        # Use create_user() to properly handle password hashing
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create an authentication token for the user
        Token.objects.create(user=user)
        return user
