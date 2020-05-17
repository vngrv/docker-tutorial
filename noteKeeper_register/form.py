from django import forms
from .models import noteKeeper

class NoteForm(forms.ModelForm):
    class Meta:
        model = noteKeeper
        fields = '__all__'
        labels = {
                "title": "Title",
                "body": "Text"
                }
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        
