from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_course),
    path('/', views.add_course),
    path('create', views.create),
    path('courses/confirm/<int:id>', views.delete_confirm),
    path('courses/confirm/<int:id>/delete', views.delete)
    
]