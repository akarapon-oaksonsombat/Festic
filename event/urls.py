from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:event_id>', views.detail, name='detail'),
    path('all', views.all, name='all'),
]