from django.contrib import admin
from .forms import ImageForm
from .models import Category, Tag, Image, User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'gender', 'email', 'password')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name', 'created_at', 'updated_at')
	readonly_fields = ('created_at', 'updated_at')


class TagAdmin(admin.ModelAdmin):
	list_display = ('category_id', 'tag_name', 'created_at', 'updated_at')
	readonly_fields = ('created_at', 'updated_at')


class ImageAdmin(admin.ModelAdmin):
	list_display = ('image_url', 'created_at', 'updated_at')
	readonly_fields = ('created_at', 'updated_at')
	form = ImageForm


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
