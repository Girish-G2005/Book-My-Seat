from django.urls import path
from .views import register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', register_user, name = 'register_user'),
    path('login/', TokenObtainPairView.as_view(), name = 'token_obtain_pair_view'),
    path('refresh/', TokenRefreshView.as_view(), name = 'refresh_view'),
]