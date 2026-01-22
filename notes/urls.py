from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = "notes"

urlpatterns = [
    path('', lambda request: redirect('login')),   # ROOT → login
    path('list/', views.note_list, name='list'),
    path('new/', views.note_create, name='create'),
    path('delete/<int:note_id>/', views.delete_note, name='delete'),
]