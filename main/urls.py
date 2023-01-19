from django.urls import path
from main import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('person/<str:pk>/', views.person_page, name='person'),
    path('delete_person/<str:pk>/', views.delete_view, name='delete_view'),
    path('create_person/', views.create_page, name='create'),
]