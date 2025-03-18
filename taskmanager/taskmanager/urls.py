from django.contrib import admin
from django.urls import path  # Removed 'include' because it's not needed
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from users import register_user, get_tokens_for_user  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),  

    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/register/', register_user, name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



