from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # 获取next参数，如果没有则默认重定向到简历列表
                next_url = request.GET.get('next', 'resumes:list')
                return redirect(next_url)
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {
        'form': form
    })

def signup_view(request):
    # 注册视图实现
    pass

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'user': request.user
    }) 