from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
def register(request):
    """register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log the user in and the redirect to homepage

            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

