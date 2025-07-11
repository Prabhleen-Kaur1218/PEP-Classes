from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, PostForm
from . import data

# Register
def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data.users.append({'username': username, 'password': password})
            request.session['username'] = username
            return redirect('home')
    return render(request, 'register.html', {'form': form})

# Login
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            for user in data.users:
                if user['username'] == uname and user['password'] == pwd:
                    request.session['username'] = uname
                    return redirect('home')
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    request.session.flush()
    return redirect('login')

# Create Post
def create_post(request):
    if 'username' not in request.session:
        return redirect('login')

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = {
                'title': form.cleaned_data['title'],
                'content': form.cleaned_data['content'],
                'author': request.session['username']
            }
            data.posts.append(post)
            return redirect('home')
    return render(request, 'create_post.html', {'form': form})

# View Posts
def home(request):
    return render(request, 'home.html', {
        'posts': data.posts,
        'user': request.session.get('username')
    })

# Delete
def delete(request):
    blog = get_object_or_404(blog, id= id)
    blog.delete()
    return redirect('create_post')