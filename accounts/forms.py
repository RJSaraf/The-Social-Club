from django import forms
from accounts.models import UserInfo
from django.contrib.auth.models import User

# blog

class UserForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('user','phone_number','gender','birth_date','country','city','state','address','profession','age','propic')

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

        }