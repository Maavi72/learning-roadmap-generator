from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roadmap/<int:goal_id>/', views.roadmap_detail, name='roadmap_detail'),
]
