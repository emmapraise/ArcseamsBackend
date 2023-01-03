from rest_framework import serializers
from api.models import *


class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        exclude = [
            "is_active",
            "is_staff",
            "date_joined",
            "last_login",
            "is_superuser",
            "groups",
            "user_permissions",
        ]

    def create(self, validated_data):
        """Create User"""

        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        phone = validated_data["phone"]
        email = validated_data["email"]
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            middle_name=validated_data["middle_name"],
            phone=phone,
            username=email,
            email=email,
            gender=validated_data["gender"],
            password=validated_data["password"],
        )
        user.save()
        return user


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        depth = 3
        exclude = ["created_at", "updated_at"]

class ImageSerializer(serializers.ModelSerializer):
    """sumary_line"""

    class Meta:
        model = Image
        exclude = ["created_at", "updated_at"]

class ShippingAddressSerializer(serializers.ModelSerializer):
    """sumary_line"""

    class Meta:
        model = ShippingAddress
        exclude = ["created_at", "updated_at"]

class DesignSerializer(serializers.ModelSerializer):
    """sumary_line"""
    class Meta:
        model = Design
        exclude = ["created_at", "updated_at"]

class OrderSerializer(serializers.ModelSerializer):
    """sumary_line"""
    
    class Meta:
        model = Orders
        # depth=1
        exclude = ["created_at", "updated_at"]
