from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserForm


# Create your views here.
def UserProfile(request, pk):
    user = User.objects.get(id=pk)
    return HttpResponse(f'<h1>{user.username}</h1>')



def SignupView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('boards:home')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)