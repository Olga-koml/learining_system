from django.contrib import admin

from .models import Lesson,  Product


admin.site.site_title = 'Админка LEARNING_SYSTEM'
admin.site.site_header = 'Администрирование сайта LEARNING_SYSTEM'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'user_list')
    search_fields = ('title', 'owner', 'user_list')
    list_filter = ('title', 'owner')

    def user_list(self, obj):
        return ", ".join([user.username for user in obj.user.all()])

    user_list.short_description = lambda obj: f'Студент, изучающие продукт "{obj.title}"'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_link', 'duration_sec', 'products_list')
    list_filter = ('name',  'duration_sec', 'products')
    search_fields = ('name', 'products__title')
    ordering = ('name',)

    def products_list(self, obj):
        return ", ".join([product.title for product in obj.products.all()])
    products_list.short_description = 'Продукты'
