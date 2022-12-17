from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r"register", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
