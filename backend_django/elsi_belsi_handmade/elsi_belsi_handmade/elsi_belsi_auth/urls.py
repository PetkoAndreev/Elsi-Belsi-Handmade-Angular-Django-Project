from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from elsi_belsi_handmade.elsi_belsi_auth.views import RegisterView, LogoutView, LoginView, ProfileGetUpdateDeleteView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LoginView.as_view(), name='login user'),
    path('logout/', LogoutView.as_view(), name='logout user'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('user/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileGetUpdateDeleteView.as_view(), name='get profile'),
)
