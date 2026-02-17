from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("", include("app.urls")),
    path("api/token/", TokenObtainPairView.as_view()),
]