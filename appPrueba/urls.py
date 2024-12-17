from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomLoginView, LoginView, ProductViewSet, CategoryViewSet,UserSignupView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import DestinationViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/signup/', UserSignupView.as_view(), name='user-signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('login/', CustomLoginView.as_view(), name='login'),
    path('api/userLogin/', LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
]