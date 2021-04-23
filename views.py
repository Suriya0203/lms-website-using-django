 from django.shortcuts import  render, redirect
from .form import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from .models import Image
from django.contrib.auth.forms import AuthenticationForm
import django.core.checks.translation
from django.contrib.auth import login
from django.contrib import messages #import messages
#from crispy_forms.helper import FormHelper
def register_request(request,*args,**kwargs):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			#return redirect("result.views.homepage")
			return HttpResponseRedirect(reverse('homepage'))
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="register.html", context={"register_form":form})
def homepage(request):
	return render(request=request, template_name="base.html")
def login_request(request,*args,**kwargs):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				#return redirect("result.views.homepage")
				return HttpResponseRedirect(reverse('homepage'))
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return HttpResponseRedirect(reverse('homepage'))
def home(request,*args,**kwargs):
	pics = Image.objects.all()
	return render(request=request, template_name="index.html", context={"pics":pics})