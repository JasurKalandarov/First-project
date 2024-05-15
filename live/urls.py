from django.urls import path
from live import views


urlpatterns = [
    path('', views.stream, name='stream')
]