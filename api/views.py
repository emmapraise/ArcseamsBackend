from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import *
from api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """The API endpoint for CRUD operations on User Model"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CustomTokenObatinPairView(TokenObtainPairView):
    """sumary_line"""

    def post(self, request, *args, **kwargs):
        """sumary_line"""

        serializer = self.get_serializer(data=request.data)
        try:
            user = get_object_or_404(User, username=request.data["username"])
            serializer.is_valid(raise_exception=True)
            status_code = status.HTTP_200_OK
            response = {
                "data": {
                    "tokens": serializer.validated_data,
                    "user": UserSerializers(user).data,
                },
                "status": "succes",
                "message": "User successfully authenticated",
            }
        except User.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                "data": {},
                "status": "failure",
                "message": "User account not found",
            }
        except TokenError:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                "data": {},
                "status": "failure",
                "message": "Token is invalid or expired",
            }

        return Response(data=response, status=status_code)


class LogoutView(APIView):
    """sumary_line"""

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """sumary_line"""

        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MeasurementViewSet(viewsets.ModelViewSet):
    """sumary_line"""
    
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes= []

class ImageViewSet(viewsets.ModelViewSet):
    """sumary_line"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = []

class ShippingAddressViewset(viewsets.ModelViewSet):
    """sumary_line"""
    
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = []

class DesignViewSet(viewsets.ModelViewSet):
    """sumary_line"""
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    permission_classes = []

class OrderViewset(viewsets.ModelViewSet):
    """This is the viewset for all action in orders"""
    
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []