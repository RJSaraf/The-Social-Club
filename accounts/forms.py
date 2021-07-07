from django import forms
from accounts.models import UserInfo
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# accounts

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name' 
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email Address'
        

class UserForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('phone_number','gender','birth_date','country','city','state','address','profession','age','propic','cover')

        widgets = {

            'birth_date':forms.DateInput(attrs={'class':'a'}),
            'age':forms.NumberInput(attrs={'class':'a'}),
            'phone_number':forms.NumberInput(attrs={'class':'w3-padding'}),
            'Profession':forms.TextInput(attrs={'class':'a'}),
            'gender':forms.TextInput(attrs={'class':'a'}),
            'country':forms.TextInput(attrs={'class':'a'}),
            'state':forms.TextInput(attrs={'class':'a'}),
            'city':forms.TextInput(attrs={'class':'a'}),
            'address':forms.Textarea(attrs={'class':'a'}),
            'propic':forms.FileInput(attrs={'class':'margin-left'}),

        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)   
        self.fields['birth_date'].label = 'Birth Date'
        self.fields['age'].label = 'Age'
        self.fields['phone_number'].label = 'Mobile'
        self.fields['profession'].label = 'Profession'
        self.fields['gender'].label = 'Gender'
        self.fields['country'].label = 'Country'
        self.fields['state'].label = 'State'
        self.fields['city'].label = 'City'
        self.fields['address'].label = 'Address'
        self.fields['propic'].label = 'Profile Image '
        self.fields['propic'].label = 'Cover Photo '

   


