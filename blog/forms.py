from django import forms
from blog.models import Post, Comment

#blog

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author','title','text','postimage')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'postcontent'}),            
        }


class CommentForm(forms.ModelForm):

        class Meta:
            model = Comment
            fields = ('author','text')

            widgets = {
                'author':forms.TextInput(attrs={'class':'textinputclass'}),
                'text':forms.Textarea(attrs={'class':'postcontent'})
    
            }