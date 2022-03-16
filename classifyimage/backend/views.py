from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from backend.forms import CategoryForm, TagForm, ImageForm
from backend.models import Category, Tag, Image


# Create your views here.
class AddCategoryView(CreateView):
	template_name = "backend/add_category.html"
	model = Category
	form_class = CategoryForm
	success_url = reverse_lazy('success')

	def form_valid(self, form):
		"""
		This method is called when valid form data has been POSTed.
		It should return an HttpResponse.
		"""
		form.save()
		return super().form_valid(form)


class AddTagView(CreateView):
	template_name = "backend/add_tag.html"
	model = Tag
	form_class = TagForm
	success_url = reverse_lazy('tag')

	def form_valid(self, form):
		"""
		This method is called when valid form data has been POSTed.
		It should return an HttpResponse.
		"""
		form.save()
		return super().form_valid(form)


class AddImageView(CreateView):
	template_name = "backend/add_image.html"
	form_class = ImageForm
	success_url = reverse_lazy('image')

	def form_valid(self, form):
		"""
		This method is called when valid form data has been POSTed.
		It should return an HttpResponse.
		"""
		form.save()
		return super().form_valid(form)


class SuccessView(TemplateView):
	template_name = 'success.html'

