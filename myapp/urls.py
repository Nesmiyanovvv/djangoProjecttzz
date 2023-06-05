from django.urls import path
from myapp import views
from myapp.views import main, profile

urlpatterns = [
    path('', views.main, name='main'),
    path('memories/', views.memories, name='memories'),
    path('memories/save/', views.memories, name='save_memory'),
    path('memories_save/', views.memories_save, name='memories_save'),
]