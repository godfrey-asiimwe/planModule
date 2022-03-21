from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_projects, name='add-projects'),
    path('all/', views.view_projects, name='view_projects'),
    path('update/<int:pk>', views.update_projects,),
    path('delete/<int:pk>', views.delete_project),
]