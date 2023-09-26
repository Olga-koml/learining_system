from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LessonViewSet, ProductViewSet, StudentPageAPIView


router = DefaultRouter()
router.register(r'lessons', LessonViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'products/<int:pk>/lessons/',
        ProductViewSet.as_view({'get': 'lessons'}),
        name='product-lessons'
        ),
    path('student-page/', StudentPageAPIView.as_view(), name='student-page'),
]
