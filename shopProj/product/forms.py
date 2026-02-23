from django import forms
from .models import Comment


class ProductComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.TextInput(attrs={'placeholder':'Add comment ...'})
        }
        labels = {
            'body': ''
        }