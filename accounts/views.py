from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been registered successfully.")
            return redirect('accounts:login')  # Ensure 'accounts:login' is defined in your URL configuration
        else:
            print(form.errors)
            messages.error(request, "Please correct the errors below and try again.")
    else:
        form = RegisterForm()
    
    # Render the template with the form
    return render(request, 'accounts/register.html', {'form': form})
  
def LoginView(request):
  form = RegisterForm()
  if request.method == 'POST':
    phone_number = request.POST.get('phone_number')
    password = request.POST.get('password')
    if not phone_number or not password:
      messages.error(request,"Phone Number and Password are required")
    user = authenticate(phone_number= phone_number, password=password)
    if user is not None:
      login(request, user)
      messages.success(request,"A user has been logged in")
      return redirect('website:index')
    else:
      messages.error(request, "Invalid phone number or password.")
  return render(request, 'accounts/login.html')

def LogoutView(request):
  logout(request)
  messages.success(request, "Successfully logged out")
  return redirect('accounts:login')
  
  
