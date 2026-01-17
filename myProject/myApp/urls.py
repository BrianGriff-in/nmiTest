from . import views
from django.urls import path
urlpatterns = [
    path(route='', view=views.home, name='home')
]
