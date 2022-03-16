from django.urls import path
from django.views.decorators.cache import cache_page

from .views import SignUpView, SignInView, HomePageView, StatsPageView, LogoutView, PasswordReset, PasswordResetDone, \
    PasswordResetConfirm, PasswordResetComplete, PasswordChange

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(redirect_authenticated_user=False), name='signin'),
    path('', HomePageView.as_view(), name='home'),
    path('stats/', StatsPageView.as_view(), name='stats'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordReset.as_view(),name='password_reset'),
    path('password-reset-done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetComplete.as_view(),name='password_reset_complete'),
    path('signin/change-password/', PasswordChange.as_view(),name='password_change'),
]
