from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from .forms import SignUpForm, createGroupForm, createPostForm
from .models import Group, Post, members
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return redirect('groups')
	return render(request,'social/home.html')

def loginView(request):
	if request.method=='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				dj_login(request, user)
				return redirect('/')
	else:
		form=AuthenticationForm()
	context = {'form':form}
	return render(request, 'login/login.html', context)

def signupView(request):
	if request.method=='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = SignUpForm()
	context = {'form':form}
	return render(request, 'login/signup.html', context)

def groupView(request):
	groups = Group.objects.all()
	context = {'groups':groups}
	return render(request,'social/groups.html', context)

def logoutView(request):
	logout(request)
	return redirect('home')

def createGroup(request):
	if request.method == 'POST':
		form = createGroupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('groups')
	else:
		form = createGroupForm()
	context = {'form':form}
	return render(request,'social/creategroup.html',context)

def posts(request, group_id):
	group = get_object_or_404(Group, id=group_id)
	posts = Post.objects.filter(group=group)
	member = members.objects.filter(group=group,user=request.user)
	len_number = len(member)
	context = {'group':group,'posts':posts,'len_number':len_number,'member':member}
	return render(request,'social/posts.html', context)

def createPost(request):
	user = User.objects.get(username=request.user.username)
	if request.method == 'POST':
		form = createPostForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = user
			form.save()
			return redirect('groups')
	else:
		form = createPostForm()
	context = {'form':form}
	return render(request,'social/createpost.html', context)

def addMembers(request,group_id):
	group = get_object_or_404(Group, id=group_id)
	user = request.user
	member = members(group=group, user=user)
	try:
		member.save()
	except:
		messages.warning(request,("Warning, already a member of {}".format(group.title)))
	return redirect('posts', group_id=group_id)

def detailPostView(request,username):
	user = get_object_or_404(User, username=username)
	print(user)
	posts = Post.objects.filter(user=user)
	context = {'posts':posts}
	return render(request,'social/detailpost.html', context)

def deleteMembers(request,group_id):
	group = get_object_or_404(Group, id=group_id)
	user = request.user
	member = members.objects.filter(group=group, user=user)
	print(member)
	try:
		member.delete()
	except:
		messages.warning(request,("You can't leave this group because you aren't in it."))
	return redirect('posts', group_id=group_id)
