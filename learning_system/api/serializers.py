from rest_framework import serializers

from courses.models import Product, Lesson, LessonView


class LessonSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_products(self, obj):
        product_titles = obj.products.values_list('title', flat=True)
        return list(product_titles)


class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    owner = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'owner',
            'lessons',
            'user']
        depth = 1

    def get_owner(self, obj):
        owner = obj.owner
        return {
            'last_name': owner.last_name,
            'first_name': owner.first_name,
        }

    def get_products(self, obj):
        product_titles = obj.products.values_list('title', flat=True)
        return list(product_titles)

    def get_user(self, obj):
        user_list = obj.user.values_list('username', flat=True)
        return list(user_list)


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = '__all__'


class StudentPageSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'owner',
            'lessons',
        ]

    def get_owner(self, obj):
        owner = obj.owner
        return {
            'last_name': owner.last_name,
            'first_name': owner.first_name,
        }

    def get_lessons(self, obj):
        user = self.context['request'].user
        lessons = obj.lessons.all()
        lesson_views = LessonView.objects.filter(user=user, lesson__in=lessons)
        lesson_views_data = []

        for lesson in lessons:
            lesson_view = lesson_views.filter(lesson=lesson).first()
            lesson_data = LessonSerializer(lesson).data
            if lesson_view:
                lesson_data.update({
                    'status': lesson_view.status,
                    'viewing_time_seconds': lesson_view.viewing_time_seconds,
                    'last_viewed_at': lesson_view.last_viewed_at
                })
            else:
                lesson_data.update({
                    'status': 'NV',
                    'viewing_time_seconds': 0,
                    'last_viewed_at': None
                })
            lesson_views_data.append(lesson_data)

        return lesson_views_data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['lessons'] = [
            {
                'id': lesson['id'],
                'name': lesson['name'],
                'video_link': lesson['video_link'],
                'duration_sec': lesson['duration_sec'],
                'status': lesson['status'],
                'viewing_time_seconds': lesson['viewing_time_seconds'],
                'last_viewed_at': lesson['last_viewed_at'],
            }
            for lesson in data['lessons']
        ]
        return data
