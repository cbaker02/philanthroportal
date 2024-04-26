# main/forms.py
from django import forms
from django.forms import TextInput,EmailInput, ModelForm
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_resized import ResizedImageField


from .models import CustomUser, Nfp, Corporation, Grant, GrantApplication, Donation

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Jane Doe', 'class':'form-control'}), max_length=100, required=True)
    from_email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'placeholder': 'janedoe@example.com', 'class':'form-control'}), required=True)
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Subject of Email','class': 'form-control'}))
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
    #email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = PhoneNumberField(region="US", label='Phone Number',required=False)
    #profile_image = ResizedImageField(size=[40,40], null=True, upload_to='photos/pfps')
    class Meta:
        model = CustomUser
        fields = ['phone','profile_image']
        
class CreateGrant(ModelForm):
    grant_name = forms.CharField(label='Grant Name', widget=forms.TextInput(attrs={'placeholder': 'Giving for Good', 'class': 'form-control'}))
    amount = forms.CharField(label='Amount', widget=forms.TextInput(attrs={'placeholder': '$500,000', 'class': 'form-control'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    due_date = forms.DateField(label='Due Date', widget=forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}))
    
    class Meta:
        model = Grant
        fields =  ['grant_name', 'amount', 'description', 'due_date']
      
class CreateGrantApplication(ModelForm):
    class Meta:
        model = GrantApplication
        fields =  ['grant', 'body', 'current_status']
        widgets = {
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'current_status' : forms.HiddenInput(),
        }
        
class UpdateNFPForm(forms.ModelForm):
    address = forms.CharField(label='Address', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    address2 = forms.CharField(max_length=200, label='Address 2', widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    city = forms.CharField(max_length=200, label='City', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    state = forms.CharField(max_length=2, label='State', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    zipCode = forms.CharField(max_length=5, label='Zip Code', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
   
    items = forms.CharField(max_length=2000, label='Items wanted for Donation', widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),required=False)
    
    class Meta:
        model = Nfp
        fields = [ 'address', 'address2', 'city', 'state', 'zipCode','items', 'bio']

class UpdateCorporationForm(forms.ModelForm):
    address = forms.CharField(label='Address', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    address2 = forms.CharField(max_length=200, label='Address 2', widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    city = forms.CharField(max_length=200, label='City', widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    state = forms.CharField(max_length=2, label='State', widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    zipCode = forms.CharField(max_length=5, label='Zip Code', widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    
    bio = forms.CharField(max_length=10000, label= 'Biography', widget=forms.Textarea(attrs={'class': 'form-control'}),required=False)
    class Meta:
        model = Corporation
        fields = ['address', 'address2', 'city', 'state', 'zipCode', 'bio']
                
class UpdateGrantApplicationStatus(forms.ModelForm):
    class Meta:
        model = GrantApplication
        fields = ['current_status']
        widgets = {'current_status' : forms.ChoiceField(choices=GrantApplication.STATUS)}

class CreateDonation(forms.ModelForm):
    class Meta:
        model = Donation
        fields =  ['nfp', 'amount']
        widgets = {
            'amount' : forms.TextInput(attrs={'class': 'form-control'}),
        }