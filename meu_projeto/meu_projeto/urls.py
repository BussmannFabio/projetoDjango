from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import CustomUserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView  # Novo endpoint opcional
)

router = DefaultRouter()
router.register(r'usuarios', CustomUserViewSet)

urlpatterns = [
  
    path('admin/', admin.site.urls),
    
    # API 
      path('api/', include([
        path('', include(router.urls)),  # endpoints de usuário
        
        # simpleJWT
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]))
    ]