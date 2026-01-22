from . import views
from django.urls import path
urlpatterns = [
    path(route='', view=views.home, name='home'), 
    path("detail/<int:id>/", views.detail, name="detail")

]
