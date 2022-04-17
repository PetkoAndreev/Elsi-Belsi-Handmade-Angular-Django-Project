from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from elsi_belsi_handmade.elsi_belsi_auth.views import RegisterView, LogoutView, LoginView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    # path('login/', LoginView.as_view(), name='login user'),
    # path('logout/', LogoutView.as_view(), name='logout user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify'),
)
