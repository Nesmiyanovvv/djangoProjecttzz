from django.urls import path
from myapp import views
from myapp.views import main, profile

urlpatterns = [
    path('', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
]