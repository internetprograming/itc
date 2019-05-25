from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request) :
  if request.method == "POST" :
    form = UserCreationForm(request.POST)
    if form.is_valid() :
      form.save()
      # first_name = form.cleaned_data.get("fname")
      # last_name = form.cleaned_data.get("lname")
      # email_address = form.cleaned_data.get("email")
      username = form.cleaned_data.get("username")
      password1 = form.cleaned_data.get("password1")
      password2 = form.cleaned_data.get("password2")
    else :
      print(form.errors)
  else :
    form = UserCreationForm()

  return render(request, "register/index.html", { 'form': form })