from django import forms
from . import models
from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = [
            'title',
            'body',
            'image',
            'featured'
            ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            #'body': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'body': TinyMCE(attrs={'class': 'form-control', 'required': True}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'required': False}),
            'featured': forms.Select(attrs={'class': 'form-control', 'required': False})
            }
        labels = {
            'title': '* Article Title',
            'body': '* Article Body',
            'image': 'Article Image',
            'featured': 'Featured Article'
            }


