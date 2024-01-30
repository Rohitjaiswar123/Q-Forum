from django import forms
from .models import Comment


class QuestionForm(forms.Form):
    TiTLe = forms.CharField()
    Tag = forms.CharField()
    Content = forms.CharField()
    
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'content', )
