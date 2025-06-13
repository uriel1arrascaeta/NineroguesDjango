from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You are now able to log in')

            return redirect('accounts:login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
