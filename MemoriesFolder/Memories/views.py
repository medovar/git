from django.shortcuts import render, redirect
from .models import Mem, Comments, Like, User
from django import forms
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.utils import timezone
import pytz, datetime

def mem(request, page_number=1):
    all_mem = Mem.objects.all()
    current_page = Paginator(all_mem, 4)
    context = {'mem' : current_page.page(page_number)}
    context['username'] = auth.get_user(request).username
    return response_url(request, 'default', context)

def memuser(request, id=1, page_number=1):
    memuser = Mem.objects.filter(user_id=id)
    current_page = Paginator(memuser, 4)
    context = {'mem' : current_page.page(page_number)}
    context['username'] = auth.get_user(request).username
    return response_url(request, 'memuser', context)

def sort(request, page_number=1, id=0):
    if id !=0:
        sort_mem = Mem.objects.filter(user_id=id).order_by('-pub_date')
        current_page = Paginator(sort_mem, 4)
        context = {'mem' : current_page.page(page_number)}
        context['username'] = auth.get_user(request).username
        return response_url(request, 'sort_dateuser', context)
    else:
        sort_mem = Mem.objects.all().order_by('-pub_date')
        current_page = Paginator(sort_mem, 4)
        context = {'mem' : current_page.page(page_number)}
        context['username'] = auth.get_user(request).username
        return response_url(request, 'sort_date', context)

def sortlike(request, page_number=1, id=0):
    if id !=0:
        sort_mem = Mem.objects.filter(user_id=id).order_by('-like_count')
        current_page = Paginator(sort_mem, 4)
        context = {'mem' : current_page.page(page_number)}
        context['username'] = auth.get_user(request).username
        return response_url(request, 'sort_likeuser', context)
    else:
        sort_mem = Mem.objects.all().order_by('-like_count')
        current_page = Paginator(sort_mem, 4)
        context = {'mem' : current_page.page(page_number)}
        context['username'] = auth.get_user(request).username
        return response_url(request, 'sort_like', context)

def addmem(request):
    if request.POST:
        text = request.POST.get('text')
        title = request.POST.get('title')
        tz = pytz.timezone('Europe/Moscow')
        date = str(datetime.datetime.now(tz))[:19]
        t = Mem(text=text, title=title, pub_date=date, user_id=auth.get_user(request).id)
        t.save()
        return redirect('/mem')
    else:
        return render(request,"Memories/addmem.html", {'username': auth.get_user(request).username})

def delmem(request, id):
    m = Mem.objects.get(pk=id)
    m.delete()
    return redirect('/mem')

def getmem(request, id=1):
    if request.POST:
        comment = request.POST.get('comment')
        t = Comments(comment=comment, user_id=auth.get_user(request).id, mem_id=id)
        t.save()
        args = {'mem' : Mem.objects.get(id=id), 'comments': Comments.objects.filter(mem_id=id), 'username': auth.get_user(request).username}
        return render(request, "Memories/getmem.html",args)
    inf = Mem.objects.get(id=id)
    inf.text = "\n\n".join(inf.text.split("\n"))
    args = {'mem': inf, 'comments': Comments.objects.filter(mem_id=id), 'username': auth.get_user(request).username}
    return render(request, "Memories/getmem.html",args)

def gen(url, context):
        if context['mem'].has_previous() is True:
            context['urlback'] = url % context['mem'].previous_page_number()
        else:
            context['urlback'] = ""
        if context['mem'].has_next() is True:
            context['urlnext'] = url % (context['mem'].next_page_number())
        else:
            context['urlnext'] = ""
        pag_block = ""
        for page in context['mem'].paginator.page_range:
            if page == context['mem'].number:
                pag_block = pag_block + "<li class='current'><a href=%s>%s</a></li>" % (url % page, page)
            else:
                pag_block = pag_block + "<li><a href=%s>%s</a></li>" % (url % page, page)
        context['urlnumber'] = pag_block
        return context

def response_url(request, idview, context):
    if idview == "default":
        url = "/page/%s"
        gen(url, context)
    if idview == "memuser":
        url="/memuser/{0}/page/%s/".format(auth.get_user(request).id)
        context['sortuser'] = "/memsortdate/memuser/{0}/page/1/".format(auth.get_user(request).id)
        context['sortlikeuser'] = "/memsortlike/memuser/{0}/page/1/".format(auth.get_user(request).id)
        gen(url, context)
    if idview == "sort_date":
        url = "/memsortdate/page/%s/"
        gen(url, context)
    if idview == "sort_dateuser":
        url = "/memsortdate/memuser/{0}/page/%s/".format(auth.get_user(request).id)
        context['sortuser'] = " "
        context['sortlikeuser'] = "/memsortlike/memuser/{0}/page/1/".format(auth.get_user(request).id)
        gen(url, context)
    if idview == "sort_like":
        url = "/memsortlike/page/%s/"
        gen(url, context)
    if idview == "sort_likeuser":
        url = "/memsortlike/memuser/{0}/page/%s/".format(auth.get_user(request).id)
        context['sortlikeuser'] = " "
        context['sortuser'] = "/memsortdate/memuser/{0}/page/1/".format(auth.get_user(request).id)
        gen(url, context)
    return render(request, 'Memories/mem.html', context)

def liking(request, id):
    st = Like.objects.filter(mem_id=id, user_id=auth.get_user(request).pk)
    if not st:
        l = Like(user_id=auth.get_user(request).pk, mem_id=id, user_st=False)
        l.save()
        m = Mem.objects.get(id=id)
        m.like_count += 1
        m.save()
        return redirect('/mem/get/%s' % id)
    if st[0].user_st == False:
        m = Mem.objects.get(id=id)
        m.like_count -= 1
        m.save()
        st[0].user_st = True
        st[0].save()
        return redirect('/mem/get/%s' % id)
    if st[0].user_st == True:
        m = Mem.objects.get(id=id)
        m.like_count += 1
        m.save()
        st[0].user_st = False
        st[0].save()
        return redirect('/mem/get/%s' % id)

def profile(request, id):
    prof = User.objects.get(id=id)
    args = {'prof': prof, 'username': auth.get_user(request).username}
    return render(request, "Memories/profile.html", args)

def profileupd(request, id):
    if request.POST:
        email = request.POST.get('email')
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        prof = User.objects.get(id=id)
        if email != "":
            prof.email = email
        if name != "":
            prof.first_name = name
        if lastname != "":
            prof.last_name = lastname
        prof.save()
        return profile(request, id)
    else:
        args = {'username': auth.get_user(request).username}
        return render(request, "Memories/profile.html", args)

'''
class RegForm(forms.Form):
    login = forms.CharField(label='Логин',required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Почта',required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='Пароль',required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    def regist(request):
        if request.method == 'POST':
            form = RegForm(request.POST)
            if form.is_valid():
                login = form.cleaned_data['login']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                p = Person(login=login, email=email, password=password)
                p.save()
                return render(request, 'Memories/regist.html', {'form1': 1})
        else:
            form = RegForm()
        return render(request, 'Memories/regist.html', {'form': form})

class AuthoForm(forms.Form):
    login = forms.CharField(label='Логин',required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Пароль',required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    def autho(request):
        if request.method == 'POST':
            form = AuthoForm(request.POST)
            if form.is_valid():
                login = form.cleaned_data['login']
                password = form.cleaned_data['password']
                try:
                    person = Person.objects.get(login=login)
                except:
                    return render(request, 'Memories/autho.html',{'form1': 1})
                else:
                    password_db = person.password
                    if password_db == password:
                        return render(request, 'Memories/autho.html',{'form2': 1})
                    else:
                        return render(request, 'Memories/autho.html',{'form1': 1})
        else:
            form = AuthoForm()
        return render(request, 'Memories/autho.html', {'form': form})
'''

