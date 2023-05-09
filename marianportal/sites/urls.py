from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views),
    path('subjects/<int:subject_id>/', views.subject_detail, name='subject_detail'),
]
    