from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm   # import user
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from .forms import UserRegisterForm

# Create your views here.
def register(request):  
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # check valid
            form.save()
            username = form.cleaned_data.get('username')   # save the username
            messages.success(request, f'Account Created for {username}!')  #flash message 
            # messages.success(request, f'Your Account has been Created! You are now able to login')  #flash message

            return redirect('login')   # url name
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})



@login_required
def profile(request):
    return render(request ,'users/profile.html' )
