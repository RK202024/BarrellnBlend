from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('generate_drink/', views.generate_drink, name='generate_drink'),
    path('drinks/', views.drink_index, name='all_drinks'),
    path('add_to_bar/', views.add_to_bar, name='add_to_bar'),
    path('bar/', views.bar, name='bar'),
    path('drinks/<int:drink_id>/', views.drink_detail, name='drink_detail'),
]