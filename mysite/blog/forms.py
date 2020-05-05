from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post  # connect models
        fields=('author','title','text')

        # now we are gonna add widgets
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment # connect models
        fields = ('author','text')

        widgets={
                    'author':forms.TextInput(attrs={'class':'textinputclass'}),
                    'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
                }
