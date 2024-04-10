from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, CustomUserCreationForm, GrantApplication, CreateGrant, CreateGrantModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# NOTE: When adding a new view/template, make sure to add it to main/urls.py
# which is different from philanthroportal/urls.py
# views in main/urls.py are referenced by philanthroportal/urls.py automatically

def home(request):
    return render(request, "home.html")

def nfps(request):
    nfps = Nfp.objects.all()

    return render(request, "nfps.html", {'nfps': nfps})

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
                user = form.cleaned_data.get('email').__str__()
                account_type = form.cleaned_data['account_type']
                print(account_type)
                
                # TODO: Change to proper redirect
                
                # NFP
                if account_type == "Non-For-Profit Organization":
                    return redirect('NFPs')
                
                # CORP
                elif account_type == "Corporation":
                    return redirect('Grant Application')
                
                # INDIVIDUAL
                else:
                    return redirect('Home')
                # messages.success(request, 'Account was created for ', user)
                #return redirect('login')
        
        context = {'form': form}
        return render(request, 'register.html', context)

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
    
def createGrantModelForm(request):
    if request.method == 'POST':
        form = CreateGrantModelForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CreateGrantModelForm
    return render(request, 'createGrant.html', {'form': form})

'''def createGrant(request):
    if request.method == 'POST':
        form = CreateGrant(request.POST)
        if form.is_valid():
            pass
    else:
        form = CreateGrant()
    return render(request, 'createGrant.html', {'form': form})'''
    
def grantApplication(request):
    #TODO: Catherine
    if request.method == 'POST':
        form = GrantApplication(request.POST)
        if form.is_valid():
            pass
    else:
        form = GrantApplication()
    return render(request, "grant_application.html", {'form': form})