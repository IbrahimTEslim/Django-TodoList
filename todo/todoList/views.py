import json
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from .models import User
from django.contrib.auth import login as login_me,logout as log_out
from django.db.utils import IntegrityError
from .models import Todo
import datetime
import hashlib

# Create your views here.

def login(request):
    if request.method == 'POST':
        if 'username' not in request.headers or 'password' not in request.headers:
            return HttpResponse('Bad request for logging in')
        usern = request.headers['username']
        pasw = request.headers['password']
        # print("\n",usern,"\n",pasw)
        m = hashlib.sha256()
        m.update(pasw.encode())
        pasw = m.hexdigest()
        try:
            user = User.objects.get(username=usern,password=pasw)
        except:
            user = None
        if user is not None:
            login_me(request,user)
            request.session.modified = True
            return HttpResponse("Logged In :}")
        else:
            return HttpResponse("Can't log in :{")
    else:
        return HttpResponse("Send your Login Credentials")


def register(request):
    if request.method == 'POST':
        if 'username' in request.headers:
            usern = request.headers['username']
            if not usern:
                return HttpResponse("Not Allowed Null Values for users names")
        else:
            return HttpResponse("Can't see a username")
        if 'password' in request.headers:
            pasw = request.headers['password']
        else:
            return HttpResponse("can't see a password")
        if 'email' in request.headers:
            email = request.headers['email']
        else:
            email = None

        m= hashlib.sha256()
        m.update(pasw.encode('utf-8'))
        pasw = m.hexdigest()

        try:
            user = User.objects.create(username=usern,password=pasw,email=email,is_staff=False)
        except IntegrityError:
            return HttpResponse("This username is already used\nchange username")
        print("\n\nuser Created: ",user,"\n\n")
        login_me(request,user)
        return HttpResponse("Registerd OK")
    else:
        return HttpResponse('send your info to register ^_^')
    

def logout(request):
    log_out(request)
    return HttpResponse("Logged Out nn")


def add_entry(request):
    if request.method == 'POST':
        text = request.headers['text']
        user_id = request.session['_auth_user_id']
        user = User.objects.get(pk=user_id)
        print("\n\n",user,"\n\n")
        Todo.objects.create(user = user,text = text,is_done=False,is_deleted=False)
        return HttpResponse("Added Succesfully")


def show_current(request):
    if request.method == 'GET':
        user_id = request.session['_auth_user_id']
        user = User.objects.get(pk=user_id)
        data = list(Todo.objects.all().filter(user = user,is_done=0,is_deleted=0).values('text','added_at').order_by('added_at'))
        
        return JsonResponse(data,safe=False)


def show_done(request):
    user = User.objects.get(pk = request.session['_auth_user_id'])
    data = list(Todo.objects.filter(user = user,is_done=1,is_deleted=0).values('text','added_at','done_at').order_by('added_at'))
    return JsonResponse(data,safe=0)


def mark_done(request,todo_id):
    item = Todo.objects.get(pk = todo_id)
    item.is_done = 1
    item.done_at = datetime.datetime.now()
    item.save()
    return HttpResponse("Updated Succesfully")


def mark_delete(request,todo_id):
    item = Todo.objects.get(pk = todo_id)
    item.is_deleted = 1
    item.save()
    return HttpResponse("Deleted Succesfully")


def show_deleted(request):
    data = list(Todo.objects.all().filter(user = User.objects.get(pk = request.session['_auth_user_id']),is_deleted = 1).values('text','added_at','id').order_by('-added_at'))

    return JsonResponse(data,safe=0)


def show_all(request):
    data = list(Todo.objects.all().filter(user = User.objects.get(pk = request.session['_auth_user_id'])).values().order_by('-last_update'))
    return JsonResponse(data,safe=0)


