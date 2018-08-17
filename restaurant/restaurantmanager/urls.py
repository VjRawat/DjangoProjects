from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('aboutus', views.aboutus),
    path('addNewMenu', views.add_new_menu_item, name='add-new-name')
]