from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Nform, Choice, Question, Post
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.contrib import auth
from django.db import models
from .form import PostForm

def site_index(request):
    forms = Nform.objects.order_by('-published_date')
    return render_to_response('polls/index.html', {'forms': forms})


def form_detail(request, pk):
    current_form = get_object_or_404(Nform, pk=pk)
    fame = current_form.fname
    latest_question_list = Question.objects.filter(for_form=fame).order_by('-pub_date')
    choice_quest_list = []
    text_quest_list = []
    form = PostForm()
    for i in range(len(latest_question_list)):
        if len(latest_question_list[i].choice_set.all()) == 0:
            text_quest_list.append(latest_question_list[i])
        else:
            choice_quest_list.append(latest_question_list[i])
    return render(request, 'polls/read_only.html', {'choice_quest_list': choice_quest_list, 'text_quest_list': text_quest_list, 'form_name': fame, 'form': form})




    # Form views
def new_form(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('polls/new_form.html', c)


def make_form(request):
    author = request.user
    fame = request.POST.get('form_name', '')
    description = request.POST.get('description', '')
    f = Nform(author=author, fname=fame, description=description, published_date=timezone.now())
    f.save()
    template = loader.get_template('polls/form.html')
    context = {
        'form_name': fame,
    }
    return HttpResponse(template.render(context, request))


def edit_form(request):
    template = loader.get_template('polls/form.html')
    current_form = Nform.objects.latest('id')
    fame = current_form.fname
    latest_question_list = Question.objects.filter(for_form=fame).order_by('-pub_date')
    choice_quest_list = []
    text_quest_list = []
    form = PostForm()
    for i in range(len(latest_question_list)):
        if len(latest_question_list[i].choice_set.all()) == 0:
            text_quest_list.append(latest_question_list[i])
        else:
            choice_quest_list.append(latest_question_list[i])
    context = {
        'latest_question_list': latest_question_list,
        'choice_quest_list': choice_quest_list,
        'text_quest_list': text_quest_list,
        'form_name': fame,
        'form': form,
    }
    return HttpResponse(template.render(context, request))







    # Generating questions views
def new_quest(request):
    c_f = Nform.objects.latest('id')
    template = loader.get_template('polls/new_quest.html')
    fame = c_f.fname
    context = {
        'form_name': fame,
    }
    return HttpResponse(template.render(context, request))

def make_quest(request):
    quest = request.POST.get('question', '')
    ch1 = request.POST.get('choice1', '')
    ch2 = request.POST.get('choice2', '')
    ch3 = request.POST.get('choice3', '')
    c_f = Nform.objects.latest('id')
    fame = c_f.fname
    q = Question(question_text=quest, for_form=fame, pub_date=timezone.now())
    q.save()
    if ch1 == '':
        return HttpResponseRedirect('/edit_form')
    elif ch2 == '':
        q.choice_set.create(choice_text=ch1, votes=0)
        return HttpResponseRedirect('/edit_form')
    elif ch3 == '':
        q.choice_set.create(choice_text=ch1, votes=0)
        q.choice_set.create(choice_text=ch2, votes=0)
        return HttpResponseRedirect('/edit_form')
    else:
        q.choice_set.create(choice_text=ch1, votes=0)
        q.choice_set.create(choice_text=ch2, votes=0)
        q.choice_set.create(choice_text=ch3, votes=0)
        return HttpResponseRedirect('/edit_form')








    # Login views
def new_user(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('polls/new_user.html', c)

def make_new_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = User.objects.create_user(username, 'admin@admin.com', password)
    return HttpResponseRedirect('/accounts/created_new_user')

def cre_n_user(request):
    return render_to_response('polls/cre_n_user.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('polls/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('polls/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('polls/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('polls/logout.html')
