from django import forms
from django.forms import TextInput,EmailInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

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

class nfpCreationForm(forms.Form):
    org_name = forms.CharField(max_length=200, label='Organization Name')
    
    address = forms.CharField(label='Address', max_length=200)
    address2 = forms.CharField(max_length=200, label='Address 2')
    city = forms.CharField(max_length=200, label='City')
    state = forms.CharField(max_length=2, label='State',)
    zipCode = forms.CharField(max_length=5, label='Zip Code')
    
    bio = forms.CharField(max_length=10000, label= 'Biography')
    items = forms.CharField(max_length=2000, label='Items wanted for Donation')
    #tags to be added later
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email']
      
class GrantApplication(forms.Form):
    nfp_name = forms.CharField(required=True, label='NFP Name', widget=forms.TextInput(attrs={'placeholder': 'NFP Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    nfp_address = forms.CharField(required=True, label='Mailing Address', widget=forms.TextInput(attrs={'placeholder': 'Mailing Address', 'style': 'width: 300px;', 'class': 'form-control'}))
    nfp_address2 = forms.CharField(required=False, label='Address Line 2', widget=forms.TextInput(attrs={'placeholder': 'Address Line 2', 'style': 'width: 300px;', 'class': 'form-control'}))
    nfp_city = forms.CharField(required=True, label='City', widget=forms.TextInput(attrs={'placeholder': 'City', 'style': 'width: 300px;', 'class': 'form-control'}))
    nfp_state = forms.CharField(required=True, label='State', widget=forms.TextInput(attrs={'placeholder': 'State', 'style': 'width: 300px;', 'class': 'form-control'}), max_length=2)
    nfp_zip = forms.CharField(required=True, label='ZIP Code', widget=forms.TextInput(attrs={'placeholder': 'Zip Code', 'style': 'width: 300px;', 'class': 'form-control'}), max_length=5)
    nfp_phone = forms.CharField(required=True, label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'style': 'width: 300px;', 'class': 'form-control'}), max_length=10)
