from django.shortcuts import render

from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import User

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            args['login_error']='Неверные данные'
            return render_to_response('LoginSys/login.html', args)
    else:
        return render_to_response('LoginSys/login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    args={}
    args.update(csrf(request))
    if request.POST:
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            email = request.POST.get('email','')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/')
    else:
        return render_to_response('LoginSys/register.html',args)
