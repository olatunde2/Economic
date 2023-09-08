from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from market.forms import CustomUserForm



def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered SuccessFully! Login to Continue")
            return redirect('/login')
    context = {'form': form}
    return render(request, "market/auth/register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already Logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login')
        return render(request, "market/auth/login.html")
    


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Success")
    return redirect("/")