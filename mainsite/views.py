from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm, AddArtistForm
from .models import Artist

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		#user = User.objects.all()
		return render(request, 'home.html')
	else:
		return redirect('login')
	
def login_user(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Logged In! Welcome!")
			return redirect('home')
	else:
		form = LoginForm()
		return render(request, 'login.html', {'login':form})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def database(request):
	if request.user.is_authenticated:
		artists = Artist.objects.all().order_by('-artist_name')
		return render(request, 'database.html', {'artists':artists})
	
def upload_data(request):
	form = AddArtistForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				upload = form.save(commit=False)
				upload.added_by = request.user
				form.save()
				messages.success(request, "Successfully Added!")
				return redirect('database')
		return render(request, 'new_data.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In!")
		return redirect('home')