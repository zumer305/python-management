from django.urls import path
from .views import project_list_create, project_detail

urlpatterns = [
    path('', project_list_create),
    path('<int:pk>/', project_detail),
]