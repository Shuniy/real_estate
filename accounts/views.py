from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        # checking password
        if password1 == password2:
            # check username
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Username already exist')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)

                    # # login after register
                    # auth.login(request. user)
                    # messages.success(request, 'You are now Logged In')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now Registered and Can log In')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    print(request.method)
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now Logged Out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
