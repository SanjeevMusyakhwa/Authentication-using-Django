from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been registered successfully.")
            return redirect('accounts:login')  # Replace 'login' with the name of your login URL
        else:
            messages.warning(request, "Something went wrong. Please check the form and try again.")
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
