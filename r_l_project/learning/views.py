# Workflow 6 ->  Templates base.html for Workflow 7 and from there everything is awesome.
from django.shortcuts import render
from learning.forms import UserInfoForm, UserProfileInfoForm

# Helper Libraies
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'learning_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def thank(request):
    return render(request,'learning_app/thank.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserInfoForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Form Validation
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() # save it directly to database, commit= True by default
            user.set_password(user.password) # Encrypted password
            user.save() # update it in database

            profile =  profile_form.save(commit=False)
            profile.user = user # One to One relation with the user_form

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserInfoForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'learning_app/registration.html',{

        'user_form':user_form,
        'profile_form':profile_form,
        'registered': registered

    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                # Log the user in.
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password)) # Debug
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'learning_app/login.html', {})


