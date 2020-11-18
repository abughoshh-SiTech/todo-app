
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<task_id>', views.delete, name="delete"),
    path('complete/<task_id>', views.complete, name="complete"),
    path('uncomplete/<task_id>', views.uncomplete, name="uncomplete"),
    path('edit/<task_id>', views.edit, name="edit"),


]
