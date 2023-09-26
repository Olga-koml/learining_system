from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courses.models import Product, Lesson, LessonView
from .serializers import (LessonSerializer, ProductSerializer,
                          LessonViewSerializer, StudentPageSerializer)


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def lessons(self, request, pk=None):
        user = self.request.user
        product = self.get_object()
        if user not in product.user.all():
            return Response(
                {'detail': 'You do not have access to this product.'},
                status=403
                )

        lessons = LessonView.objects.filter(lesson__products=product)
        serializer = LessonViewSerializer(lessons, many=True)
        return Response(serializer.data)


class StudentPageAPIView(generics.ListAPIView):
    serializer_class = StudentPageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(user=user).prefetch_related('lessons')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = serializer.data
        return Response(response_data)
