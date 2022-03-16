from django.contrib import admin
from django.urls import path
from backend.views import AddCategoryView, SuccessView, AddTagView, AddImageView

urlpatterns = [
	path('category/success/', SuccessView.as_view(), name='success'),
	path('category/', AddCategoryView.as_view(), name='category'),
	path('post/ajax/category', AddCategoryView.as_view(), name="post_participant"),
	path('tag/', AddTagView.as_view(), name='tag'),
	path('image/', AddImageView.as_view(), name='image'),
]
