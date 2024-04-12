from django.db import migrations, models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# NOTE: After adding or editing a model, remember to enter in the terminal:
#   python3 manage.py makemigrations
#   python3 manage.py migrate
# If you are adding a new model or removing an old model, make the appropriate
# changes to admin.py as well before messing with the terminal. Django will not
# tell you whether or not you have done this, so please never forget to do so
# for the sake of your future sanity.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique = True, max_length=200, null=True)

    name = models.CharField(max_length=200, null=True)
    phone = PhoneNumberField(blank=True, default='(000)000-000')

    profile_image = models.ImageField(null=True)
    ACCT_TYPE = (('Non-For-Profit Organization', 'Non-For-Profit Organization'), ('Individual', 'Individual'), ('Corporation', 'Corporation'))
    account_type = models.CharField(max_length = 200, choices = ACCT_TYPE, default = 'Individual')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
        
class Nfp(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True) # Delete profile when user is deleted

    address = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=2, null=True)
    zipCode = models.CharField(max_length=5, null=True)
    
    org_name = models.CharField(max_length=200, null=True)
    bio = models.TextField(max_length=1000, null=True)
    items = models.CharField(max_length=2000, null=True, blank=True)
    #tags to be added later
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.org_name 

class Corporation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)

    address = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=2, null=True)
    zipCode = models.CharField(max_length=5, null=True)
    
    corp_name = models.CharField(max_length=200, null=True)
    bio = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.corp_name