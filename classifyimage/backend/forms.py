import re
from django import forms
from backend.models import Category, Tag, Image


class CategoryForm(forms.ModelForm):
	"""
	Create CategoryForm class for Category model.
	"""
	category_name = forms.CharField(max_length=25)

	class Meta:
		model = Category
		fields = '__all__'

	def clean(self):
		"""
		Override clean method to add validation.
		"""
		cleaned_data = super().clean()
		category = cleaned_data.get('category_name')

		if category:
			if Category.objects.exclude(pk=self.instance.pk).filter(category_name=category).exists():
				self.add_error("category_name",
				               'Category "' + category + '" is already exists, please add different category name.')
			elif not category.isalpha():
				self.add_error("category_name", "Category name must contain only letters.")
			elif len(category) < 2:
				self.add_error("category_name", "Category name must be greater than 1 letter.")


class TagForm(forms.ModelForm):
	"""
	Create TagForm class for Tag model.
	"""
	# category = forms.ModelChoiceField(queryset=Category.objects.all())
	tag_name = forms.CharField(max_length=25)

	class Meta:
		model = Tag
		fields = '__all__'

	def clean(self):
		"""
		Override clean method to add validation.
		"""
		cleaned_data = super().clean()
		category = cleaned_data.get('category')
		tag_name = cleaned_data.get('tag_name')
		datas = Tag.objects.all()
		for data in datas:
			if str(data.category) == str(category) and str(tag_name) == str(str(data.tag_name)):
				self.add_error("tag_name", 'Tag "' + tag_name + '" is already exists in "' + str(
					category).lower() + '" category, please add different tag name.')
				break

		if tag_name:
			if not tag_name.isalpha():
				self.add_error("tag_name", "Tag name must contain only letters.")

			elif len(tag_name) < 2:
				self.add_error("tag_name", "Tag name must be greater than 1 letter.")


class ImageForm(forms.ModelForm):
	"""
	Create ImageForm class for Image model.
	"""

	def __init__(self, *args, **kwargs):
		super(ImageForm, self).__init__(*args, **kwargs)
		self.fields['caption'].required = False
		self.fields['description'].required = False
		self.fields['altertext'].required = False

	class Meta:
		model = Image
		fields = ['tag', 'image_url', 'image_name', 'title', 'caption', 'description', 'altertext']
