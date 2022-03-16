from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from backend.models import *

GENDER_CHOICES = (
	('Male', 'Male'),
	('Female', 'Female'),
	('other', 'other'),
)
phone_number_regex = RegexValidator(r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
                                    message="Enter a valid phone number.")


class SignupForm(UserCreationForm):
	"""
	Create form class to edit inbuilt field and add new field which are not exist in inbuilt user model.
	"""
	gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
	phone_number = forms.CharField(max_length=14, validators=[phone_number_regex], required=True)
	username = forms.CharField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	password2 = forms.CharField(widget=forms.PasswordInput(), label="Password confirmation")

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'gender', 'email', 'phone_number', 'password1', 'password2']

	def clean(self):
		"""
		Override clean method to add validation.
		"""
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		first_name = cleaned_data.get('first_name')
		last_name = cleaned_data.get('last_name')

		if username:
			if not username.isalpha():
				self.add_error("username", "User name must contain only letters.")
			elif len(username) < 2:
				self.add_error("username", "User name must be greater than 1 letter.")

		if first_name:
			if not first_name.isalpha():
				self.add_error("first_name", "First name must contain only letters.")
			elif len(username) < 2:
				self.add_error("first_name", "First name must be greater than 1 letter.")

		if last_name:
			if not last_name.isalpha():
				self.add_error("last_name", "First name must contain only letters.")
			elif len(last_name) < 2:
				self.add_error("last_name", "First name must be greater than 1 letter.")

		if first_name and last_name:
			if first_name == last_name:
				self.add_error("last_name", "First name and last name must be different.")


class PasswordResetForm(PasswordResetForm):
	"""
	Create form class to edit inbuilt PasswordResetForm class.
	"""
	def clean_email(self):
		"""
		Override clean method to add validation.
		"""
		email = self.cleaned_data['email']
		if not User.objects.filter(email__iexact=email, is_active=True).exists():
			raise ValidationError("There is no user registered with the specified email address!")

		return email
