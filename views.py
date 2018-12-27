# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm

from .models import blog_posts

# Create your views here.
def index(request):
	#return HttpResponse('Hello Pavan!')
	return render(request, 'index.html', {'title' : 'Home'})
	
def about(request):
	#return HttpResponse('Hello Pavan!')
	return render(request, 'about.html', {'title' : 'About'})
	
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('signup')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form,'title' : 'Signup'})
	
def login(request):
	return render(request, 'login.html', {'title' : 'Login'})
	
@login_required(login_url='/login/')
def profile(request):
	return render(request, 'profile.html', {'title' : 'Profile'})
	
	
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('data')
    return render(request, 'post_form.html', {'form': form})
	
def data(request):
	Website = blog_posts.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(Website, 3)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
		# context = {
		# 'title' : 'Dynamic',
		# 'website' : Website,
		# 'users': users
	# }
	return render(request, 'data.html', { 'users': users,'title' : 'Dynamic Content' })
	
def details(request, id):
	Content = blog_posts.objects.get(id=id)
	context = {
		'content' : Content,
		'title' : 'Content Details'
	}
	return render(request, 'details.html', context)
	
def update(request, pk):
    post = get_object_or_404(blog_posts, pk=pk)
    form = blog_posts.objects.get(id=pk)
    return render(request, 'edit.html', {'form': form})
	
def edit(request,pk):
	forme = get_object_or_404(blog_posts, id=pk)
	form = PostForm(request.POST or None, instance=forme)
	if form.is_valid():
		form.save()
        return redirect('data')
		
def delete(request,pk):
	forme = get_object_or_404(blog_posts, id=pk)
	if 'POST' == request.method:
		forme.delete()
		return redirect('data')
	return render(request, 'delete.html', {'object':forme,'title' : 'Delete Content'})

