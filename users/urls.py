from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from users.api import UserApiViewSet, CustomTokenObtainPairView
from users.views import (
    IndexView, LoginView, UserView, UserRegisterView, UserChangeView, custom_logout,
)


router = DefaultRouter()
router.register(r'users', UserApiViewSet, basename='user-registration')


urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', IndexView.as_view(), name='index'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
    path('user/<int:pk>/change', UserChangeView.as_view(), name='userchange'),
    path('login/', LoginView.as_view(), name='userlogin'),
    path('cadastro', UserRegisterView.as_view(), name='userregister'),
    path('logout/', custom_logout, name='logout'),
]
