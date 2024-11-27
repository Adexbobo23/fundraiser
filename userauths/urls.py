from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('sign-in/', views.signin, name='sign-in'),
  path('logout/', views.logout_user, name='logout'),
  path('sign-up/', views.signup, name='sign-up'),
  path('profile/', views.profile, name= 'profile'),
  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]