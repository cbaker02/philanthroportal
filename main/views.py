#main/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.

# NOTE: When adding a new view/template, make sure to add it to main/urls.py
# which is different from philanthroportal/urls.py
# views in main/urls.py are referenced by philanthroportal/urls.py automatically

def home(request):
    return render(request, "home.html")

def nfps(request):
    nfps_list = Nfp.objects.all()

    return render(request, "nfps.html", {'nfps_list': nfps_list})

def contactus(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contactus.html", {'form': form})

def successView(request):
    # TODO: Update Success Destination
    return render(request, "contact_success.html")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = CustomUserCreationForm()
        
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()

                account_type = form.cleaned_data['account_type']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password1']
                account= authenticate(request, email=email,password=password)
                
                # NFP
                if account_type == "Non-For-Profit Organization":
                    return redirect('NFP Register')
                
                # CORP
                elif account_type == "Corporation":
                    return redirect('Corp Register')
                
                # INDVIDUAL
                else:
                    account= authenticate(request, email=email,password=password)
                    login(request,account)
                    return redirect ('Home')
        
        context = {'form': form}
        return render(request, 'register.html', context)
    
def nfpRegister(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = nfpCreationForm()
        if request.method == 'POST':
            form = nfpCreationForm(request.POST)
            if form.is_valid():
                
                user = CustomUser.objects.order_by('-id')[0]
                address = form.cleaned_data['address']
                address2 = form.cleaned_data['address2']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                zipCode = form.cleaned_data['zipCode']
                org_name = form.cleaned_data['org_name']
                bio = form.cleaned_data['bio']
                
                nfp = Nfp(user=user,address=address, address2=address2, city=city, state=state, zipCode=zipCode,
                      org_name=org_name, bio=bio,)
                nfp.save()

                if user is not None:
                    login(request,user)
                    return redirect ('NFPs')
                else:
                    return redirect('Home')
            
        context = {'form': form}
        return render(request, "nfpRegister.html", context)
    
# TODO: Fill out and change the return
def corpRegister(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = corpCreationForm()
        
        if request.method == 'POST':
            form = corpCreationForm(request.POST)
            if form.is_valid():
                #form.save()
                user = CustomUser.objects.order_by('-id')[0]
                address = form.cleaned_data['address']
                address2 = form.cleaned_data['address2']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                zipCode = form.cleaned_data['zipCode']
            
                corp_name = form.cleaned_data['corp_name']
                bio = form.cleaned_data['bio']

                corp = Corporation(user=user,address=address, address2=address2, city=city, state=state, zipCode=zipCode,
                      corp_name=corp_name, bio=bio,)
                corp.save()
            
                if user is not None:
                    login(request,user)
                    return redirect ('NFPs')
                else:
                    return redirect('Home')
        
        context = {'form': form}
        return render(request, 'corpRegister.html', context)

def loginPage(request):
    # TODO: Update destination 
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request, 'Email OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('Home')
    else:
        return redirect('login')
    
def createGrant(request):
    if (request.user.is_authenticated):
        
        if (request.user.account_type == 'Corporation' ):

            if request.method == 'POST':
                form = CreateGrant(request.POST)
                if form.is_valid():
                    
                    #This creates the grant object and saves it to the database
                    grant = form.save()
                    messages.success(request, 'Grant created: ' + grant.grant_name)
            else:
                form = CreateGrant
            return render(request, 'createGrant.html', {'form': form})
        else: 
            # Try to remove after permissions are established
            return redirect('Home')
    else: 
        return redirect('Home')
    
def grantApplication(request):
    if (request.user.is_authenticated):
        
        if (request.user.account_type == 'Non-For-Profit Organization'):
    
            #TODO: Catherine
            if request.method == 'POST':
                form = CreateGrantApplication(request.POST)
                if form.is_valid():
                    grant_application = form.save()
                    messages.success(request, 'Application Submitted')
                    return redirect(request, "grants.html", {'grant_list': grant_list})
            else:
                form = CreateGrantApplication
            return render(request, "grant_application.html", {'form': form})
        else: 
            # Try to remove after permissions are established
            return redirect('Home')
    else: 
        return redirect('Home')
    
def grant_list(request):
    grant_list = Grant.objects.all()

    return render(request, "grants.html", {'grant_list': grant_list})

def my_grants(request):
    if (request.user.is_authenticated):
        
        if (request.user.account_type == 'Corporation' ):
            return render(request, 'my_grants.html')
        else: 
            # Try to remove after permissions are established
            return redirect('Home')
    else: 
        return redirect('Home')
    
def my_applications(request):
    if (request.user.is_authenticated):
        
        if (request.user.account_type == 'Non-For-Profit Organization' ):
            return render(request, 'my_applications.html')
        else: 
            # Try to remove after permissions are established
            return redirect('Home')
    else: 
        return redirect('Home')
    
def nfp_donation(request):
    if (request.user.is_authenticated):
        
        if (request.user.account_type == 'Non-For-Profit Organization' ):
            return render(request, 'nfp_donation.html')
        else: 
            # Try to remove after permissions are established
            return redirect('Home')
    else: 
        return redirect('Home')
    
def indv_donation(request):
    if (request.user.is_authenticated):
        
        if (request.user.account_type == 'Individual' ):
            return render(request, 'indv_donation.html')
        else: 
            # Try to remove after permissions are established
            return redirect('Home')
    else: 
        return redirect('Home')

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name='change_password.html'
    success_message= "Successfully Changed your Password"
    success_url=reverse_lazy('home')
    
@login_required 
def profile(request):
    context = {}
    nfp_form = None
    corp_form = None
    if request.method == 'POST':
        user_form= CustomUserChangeForm(request.POST, instance=request.user)

        if request.user.account_type == 'Individual':
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='users-profile')
        elif request.user.account_type == 'Non-For-Profit Organization':
            nfp_form= UpdateNFPForm(request.POST, instance=request.user.nfp)
            if nfp_form.is_valid() and user_form.is_valid():
                user_form.save()
                nfp_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='users-profile')
        elif request.user.account_type == 'Corporation':
            corp_form=UpdateCorporationForm(request.POST, instance=request.user.corporation)
            if user_form.is_valid() and corp_form.is_valid():
                user_form.save()
                corp_form.save()
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='users-profile')
    else:
        user_form= CustomUserChangeForm(instance=request.user)
        if request.user.account_type == 'Non-For-Profit Organization':
            nfp_form= UpdateNFPForm(instance=request.user.nfp)
        elif request.user.account_type == 'Corporation':
            corp_form=UpdateCorporationForm(instance=request.user.corporation)
        
    
    context.update({
        'user_form': user_form,
        'nfp_form': nfp_form, 
        'corp_form': corp_form})

    return render(request, 'profile.html', context)

