from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserFormRegister
# Create your views here.


def logoutUser(request):
    logout(request)
    messages.info(request, 'You are deconnected')
    return redirect('login')


def registerUser(request):

    if request.user.is_authenticated:
        return redirect('list_of_articles')

    form = UserFormRegister()

    if request.method == "POST":
        form = UserFormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, 'Account successfully created')

            login(request, user)
            return redirect('list_of_articles')

    data = {'form': form, 'page': 'Register'}
    view = 'account/login.html'

    return render(request, context=data, template_name=view)


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('list_of_articles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist !')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User Connected')
            return redirect('list_of_articles')
        else:
            messages.warning(request, 'Username or password is incorrect !')

    return render(request, 'account/login.html', {'page': 'Login'})
