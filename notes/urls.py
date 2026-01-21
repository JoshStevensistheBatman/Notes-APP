from django.urls import path
from . import views

app_name = "notes"  # optional but recommended

urlpatterns = [
    path('', views.note_list, name='list'),        # homepage
    path('new/', views.note_create, name='create'),
    path('delete/<int:note_id>/', views.delete_note, name='delete'),
]