from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "author"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    # Ghost text placeholder
                    "placeholder": "Note Title"
                }
            ),
            "content": forms.Textarea(
                attrs={
                    # Ghost text placeholder
                    "placeholder": "Note. . .",
                    "rows": 4,
                }
            ),
            "author": forms.TextInput(
                # Ghost text placeholder
                attrs={"placeholder": "Name - (Optional)"}
            ),
        }
