from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login , logout

def SignupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return HttpResponse("user created")
    form = UserCreationForm
    return render(request , 'accounts/signup.html' , {'form' : form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect('/testapp')
    form = AuthenticationForm()
    return render(request , 'accounts/login.html' , {'form' : form}) 

def LogoutView(request):
    if request.method == "POST":
        logout(request)    
        return redirect('/testapp')