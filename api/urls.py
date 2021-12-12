from django.urls import path

from api import views

urlpatterns = [
    path('a/', views.add_url, name='add_url'),
    path('s/<path:code>', views.show_url, name='show_url'),
]
