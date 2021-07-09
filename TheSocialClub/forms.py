from django import forms
from TheSocialClub import models
from django.contrib.auth.models import User

# TheSocialClub

class PostForm(forms.ModelForm):

    class Meta:
        fields = ("message",'postimage')
        model = models.Post

        widgets = {
         
            'message':forms.Textarea(attrs={'class':'post-text', 'placeholder': 'Whats on your mind!'}),
            'postimage':forms.FileInput(attrs={'class':'postimage'}),

        }
        
    def __init__(self,*args,**kwargs):
        super(PostForm, self).__init__(*args,**kwargs)   
        self.fields['message'].label = ''
        self.fields['postimage'].label = 'Add to your post'
    


class GroupForm(forms.ModelForm):
    
    class Meta:
        fields = ('name', 'discription', 'groupimage')
        model = models.Group

class ChatForm(forms.ModelForm):

    class Meta:
        fields = ('image', 'msg_content',)
        model = models.PrivateMessage

        widgets = {
         
            'msg_content':forms.Textarea(attrs={'class':'msg_content', 'placeholder': 'Type a message', 'rows':4, 'cols':15, 'id':'msg-text'}),
            'image':forms.ClearableFileInput(attrs={'class':'image',}),
        }
        
    def __init__(self,*args,**kwargs):
        super(ChatForm, self).__init__(*args,**kwargs)   
        self.fields['msg_content'].label = ''
        self.fields['image'].label = ''