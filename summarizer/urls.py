from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_view, name='upload'),
    path('summary/', views.summary_view, name='summary'),  # New summary page
]
