from rest_framework import serializers
from api.models import *


class ReadWriteSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.

    Set read_serializer_class and write_serializer_class attributes on a
    viewset.
    """

    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
            "'%s' should either include a `read_serializer_class` "
            "attribute, or override the `get_read_serializer_class()` "
            "method. " % self.__class__.__name__
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` "
            "attribute, or override the `get_write_serializer_class()` "
            "method. " % self.__class__.__name__
        )
        return self.write_serializer_class


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
