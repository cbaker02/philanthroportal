from django.db import migrations, models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid

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
    email = models.CharField(unique = True, max_length=200, null=True)

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)

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
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=2, null=True)
    zipCode = models.CharField(max_length=5, null=True)
    
    org_name = models.CharField(max_length=200, null=True)
    bio = models.TextField(max_length=1000, null=True)
    items = models.CharField(max_length=2000, null=True)
    #tags to be added later
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.org_name 

class Corporation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)

    address = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=2, null=True)
    zipCode = models.CharField(max_length=5, null=True)
    
    corp_name = models.CharField(max_length=200, null=True)
    bio = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.corp_name

class Grant(models.Model):
    
    grant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    grant_name = models.CharField(max_length=200, null=True)

    amount = models.DecimalField(max_digits=19, decimal_places=4, null=True)
    corp = models.ForeignKey(Corporation, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, null=True)
    due_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.grant_name
    
class GrantApplication(models.Model):

    app_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, null=True)
    nfp = models.ForeignKey(Nfp, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=1000, null=True)
    
    STATUS = (('Pending', 'PENDING'), ('Accepted', 'ACCEPTED'), ('Rejected', 'REJECTED'))
    
    current_status =  models.CharField(max_length = 200, choices = STATUS, default = 'Pending')
    status_changed = models.DateTimeField(null=True, editable=True, blank=True)

    def __str__(self):
        return self.grant.grant_name + " application - " + self.nfp.org_name