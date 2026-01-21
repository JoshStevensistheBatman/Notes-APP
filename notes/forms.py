from django import forms
from .models import Note  # import the model

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]  # Only title and content