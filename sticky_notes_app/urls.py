from django.urls import path
from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),          # List all notes
    path("note/<int:pk>/", views.note_detail, name="note_detail"),  # Note details
    path("note/create/", views.note_create, name="note_create"),    # Create note
    path("note/<int:pk>/update/", views.note_update, name="note_update"),  # Update note
    path("note/<int:pk>/delete/", views.note_delete, name="note_delete"),  # Delete note
]
