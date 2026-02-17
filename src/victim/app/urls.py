from django.urls import path
from .views import login_view, vulnerable_page

urlpatterns = [
    path("", login_view),
    path("vuln/", vulnerable_page),
]