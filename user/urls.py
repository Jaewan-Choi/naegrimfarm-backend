from django.urls import path

from .views import UserView
from rest_framework_simplejwt.views import TokenRefreshView # JWT refresh 토큰 발급 view 인증토큰을 재발급받기위한 또 다른 토큰 
from user.views import FarmTokenObtainPairView, UserPointView


urlpatterns = [
    path('', UserView.as_view()),
    path('api/farm/token/', FarmTokenObtainPairView.as_view(), name='farm_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userpoint/', UserPointView.as_view()),
]