from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from api import views

router = routers.DefaultRouter()
router.register(r"register", views.UserViewSet)
router.register(r"measurement", views.MeasurementViewSet)
router.register(r"shippingaddress", views.ShippingAddressViewset)
router.register(r"image", views.ImageViewSet)
router.register(r"design", views.DesignViewSet)
router.register(r"order", views.OrderViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.CustomTokenObatinPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", views.LogoutView.as_view(), name="auth_logout"),
]
