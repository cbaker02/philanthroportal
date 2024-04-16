# main/forms.py
from django import forms
from django.forms import TextInput,EmailInput, ModelForm
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Nfp, Corporation, Grant, GrantApplication

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Jane Doe', 'class':'form-control'}), max_length=100, required=True)
    from_email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'placeholder': 'janedoe@example.com', 'class':'form-control'}), required=True)
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter message here...', 'class':'form-control'}), required=True)

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(label='Full Name',  widget=forms.TextInput(attrs={'placeholder': 'Jane Doe', 'class':'form-control'}), max_length=100, required=True)
    phone = PhoneNumberField(region="US", label='Phone Number')
    email = forms.EmailField()
    CHOICES = (('Non-For-Profit Organization', 'Non-For-Profit Organization'), ('Individual', 'Individual'), ('Corporation', 'Corporation'))
    account_type = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = CustomUser
        fields = ['name', 'phone', 'email', 'password1', 'password2', 'account_type']

class nfpCreationForm(forms.Form):
    org_name = forms.CharField(label='Organization Name', widget=forms.TextInput(attrs={'placeholder': 'Organization Name', 'class': 'form-control'}),max_length=200, required=True)
    address = forms.CharField(label='Address', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Address','class': 'form-control'}))
    address2 = forms.CharField(max_length=200, label='Address 2', widget=forms.TextInput(attrs={'placeholder': 'Address Continued', 'class': 'form-control'}), required=False)
    city = forms.CharField(max_length=200, label='City', widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(max_length=2, label='State', widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zipCode = forms.CharField(max_length=5, label='Zip Code', widget=forms.TextInput(attrs={'placeholder': 'Zip Code','class': 'form-control'}))
    
    bio = forms.CharField(max_length=10000, label= 'Biography', widget=forms.Textarea(attrs={'placeholder': 'Tell us about your organization!','class': 'form-control'}))
    #items = forms.CharField(max_length=2000, label='Items wanted for Donation', widget=forms.Textarea(attrs={'class': 'form-control'}))
    #tags to be added later
    class Meta:
        model = Nfp
        fields = ['org_name', 'address', 'address2', 'city', 'state', 'zipCode', 'bio']


class corpCreationForm(forms.Form):
    corp_name = forms.CharField(label='Corporation Name', widget=forms.TextInput(attrs={'placeholder': 'Corporation Name', 'class': 'form-control'}),max_length=200, required=True)
    address = forms.CharField(label='Address', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Address','class': 'form-control'}))
    address2 = forms.CharField(max_length=200, label='Address 2', widget=forms.TextInput(attrs={'placeholder': 'Address 2','class': 'form-control'}),required=False)
    city = forms.CharField(max_length=200, label='City', widget=forms.TextInput(attrs={'placeholder': 'City','class': 'form-control'}))
    state = forms.CharField(max_length=2, label='State', widget=forms.TextInput(attrs={'placeholder': 'State','class': 'form-control'}))
    zipCode = forms.CharField(max_length=5, label='Zip Code', widget=forms.TextInput(attrs={'placeholder': 'Zip Code','class': 'form-control'}))
    
    bio = forms.CharField(max_length=10000, label= 'Biography', widget=forms.Textarea(attrs={'placeholder': 'Tell us about your company!','class': 'form-control'}))
    class Meta:
        model = Corporation
        fields = ['corp_name', 'address', 'address2', 'city', 'state', 'zipCode', 'bio']

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
        fields =  ['grant', 'body']
        widgets = {
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }