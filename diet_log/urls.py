from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),
]