from django import forms 
from django.forms import ModelForm, fields
from .models import Note 
 
 
class NoteForm(forms.ModelForm): 
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder":"Enter Title"
    }))
    context = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
         "class": "form-control", "placeholder":"Enter Notes", "rows":"8"
    }))

    """ 
    Form for creating and updating Post objects. 
 
    Fields: 
    - title: CharField for the post title. 
    - content: TextField for the post content. 
 
    Meta class: 
    - Defines the model to use (Post) and the fields to include in the 
form. 
 
    :param forms.ModelForm: Django's ModelForm class. 
    """ 
 
    class Meta: 
        model = Note 
        fields = ["title", "content"]