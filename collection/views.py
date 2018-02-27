from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import User, Question
# Other Plugin
import json

# Create your views here.

def index(request):
	return render(request, 'index.html', {
		'title': 'Welcome',
		'info': 'Base'
	})

def quiz(request):
    return render(request, 'quiz.html', {
			'title': 'Quiz',
			'info':"Quiz"
		})


def collect(request):
    return render(request, 'collect.html', {
			'title': 'Collection',
			'info':"Base"
		})
    

def init_register(request):
    return render(request, 'register.html', {
			'title': 'Signup',
			'info':"注册"
		})
    

def init_login(request):
    return render(request, 'login.html', {
			'title': 'login',
			'info':"登录"
		})



def register(request):
	status = 0
	if request.method == "POST":
		username = request.POST.get('username')
		useremail = request.POST.get('email')
		userpassword = request.POST.get('password')
		try:
			is_resist_user = User.objects.get(user_name=username)
			if is_resist_user:
				results = "Already have this name, please input another."
		except User.DoesNotExist:
			try:
				user = User(user_name=username, user_email=useremail, user_password=userpassword)
				user.save()
				results = "Welcome!"
				status = 20
			except:
				results = "Create user error"

	if status == 20:
		user_name = user.user_name


		return render(request, 'index.html', {
			'title': 'Home',
			'username': user_name,
			'user': user,
			'info': 'base'
		})
	else:
		return render(request, 'register.html', {
			'title': 'Login',
			'other': results
		})

def login(request):
	status = 0
	if request.method == "POST":
		try:
			m = User.objects.get(user_name=request.POST.get('username'))
			if m.user_password == request.POST.get('password'):
				msg = "You're logged in."
				status = 20
			else:
				msg = "Wrong password"
		except User.DoesNotExist:
			msg = "Wrong user name, please register!"

	else:
		msg = "Wrong request"
	if status == 20:
		user_name = m.user_name
		return render(request, 'index.html', {
			'title': 'Home',
			'username': user_name,
			'user': m,
			'info': 'base'
		})
	else:
		return render(request, 'login.html', {
			'title': 'Login',
			'other': msg
		})
