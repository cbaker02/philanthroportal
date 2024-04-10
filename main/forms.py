from django import forms
from django.forms import TextInput, EmailInput, ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Nfp, Grant, GrantApplication

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Jane Doe', 'class':'form-control'}), max_length=100, required=True)
    from_email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'placeholder': 'janedoe@example.com', 'class':'form-control'}), required=True)
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter message here...', 'class':'form-control'}), required=True)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    CHOICES = (('Non-For-Profit Organization', 'Non-For-Profit Organization'), ('Individual', 'Individual'), ('Corporation', 'Corporation'))
    account_type = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = CustomUser
        fields = ['name', 'phone', 'email', 'password1', 'password2', 'account_type']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email']

class CreateGrant(ModelForm):
    class Meta:
        model = Grant
        fields =  ['grant_name', 'amount', 'description', 'due_date']
        widgets = {
            'grant_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'amount' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
        }
      
class CreateGrantApplication(ModelForm):
    class Meta:
        model = GrantApplication
        fields =  ['grant', 'nfp', 'body']
        widgets = {
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }

'''class CreateGrantApplicationModelForm(ModelForm):
    class Meta:
        model = GrantApplication
        fields =  ['grant', 'nfp', 'body', 'status']'''