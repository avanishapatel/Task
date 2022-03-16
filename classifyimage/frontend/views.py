from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Count
from backend.models import Category, Tag, Image, ImageTag
from django.views.decorators.cache import cache_control

from .forms import SignupForm, PasswordResetForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView


# Create your views here.

class SignUpView(CreateView):
    """
    SignUpView for register new user.
    """
    template_name = "frontend/user_signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        form.save()
        return super().form_valid(form)


class SignInView(LoginView):
    """
    LogoutView for user login.
    If user successfully login then user redirect to home page.
    """
    template_name = "frontend/user_login.html"
    redirect_field_name = reverse_lazy("home")


class HomePageView(View):
    """
    HomePageView return all the category, tag, images also you post the images according to category and tag.
    This home page only show if user login.
    """
    template_name = "frontend/home_page.html"
    context = {
        "category": Category.objects.all(),
        "tag": Tag.objects.all(),
        "image": Image.objects.all()
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # return true
            return render(request, self.template_name, self.context)
        else:
            return redirect('signin')

    def post(self, request, *args, **kwargs):
        category = request.POST.get('categories')
        tag = request.POST.get('tag')
        images = request.POST.getlist('checked-image')
        try:
            if category and tag and images:
                for image in request.POST.getlist('checked-image'):
                    ImageTag.objects.bulk_create(
                        [ImageTag(category_id=category, tag_id=tag, image_id=image)])
                return render(request, self.template_name, self.context)
            else:
                return render(request, self.template_name, self.context)
        except:
            return render(request, self.template_name, self.context)


class StatsPageView(View):
    """
    StatsPageView view return total number of image by tag if user login.

    extra:
    # SELECT tag_name, count(tag_id) FROM classifyimage.tags right JOIN classifyimage.images_tag ON tags.id =
    # images_tag.tag_id group by tag_id;

    # queryset = ImageTag.objects.values('tag_id').annotate(count=Count('tag_id'))
    # print("queryset",queryset)
    """
    template_name = "frontend/stats.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # return true
            image = Image.objects.filter(tag__isnull=False).values('tag__tag_name').annotate(count=Count('tag'))
            context = {
                "image": image,
            }
            return render(request, self.template_name, context)
        else:
            return redirect('signin')


class LogoutView(View):
    """
    LogoutView view for logout.
    """

    @staticmethod
    @cache_control(max_age=0, no_cache=True, must_revalidate=True, no_store=True)
    def get(request, *args, **kwargs):
        logout(request)
        return redirect('signin')


class PasswordReset(PasswordResetView):
    """
    PasswordReset view for reset password when user forgot password at the time of login.
    """
    form_class = PasswordResetForm
    template_name = 'frontend/forgot_password.html'
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """
    PasswordResetDone view to confirm password reset is done.
    """
    template_name = 'frontend/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """
    PasswordResetConfirm view to confirm password reset.
    """
    template_name = 'frontend/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    form_valid_message = "Your password was changed!"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PasswordResetComplete(PasswordResetCompleteView):
    """
    PasswordResetComplete view to confirm password reset completed.
    """
    template_name = 'frontend/password_reset_complete.html'


class PasswordChange(PasswordChangeView):
    """
    PasswordChange view for change password when user login and want to change current password.
    """
    form_class = PasswordChangeForm
    template_name = 'frontend/password_change.html'
    success_url = reverse_lazy('logout')
    form_valid_message = "Your password was changed!"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
