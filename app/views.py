from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import Question, Answer, Tags


def index(request):
    q_list = Question.objects.new_questions()
    t_list = Tags.objects.all().select_related()
    page = request.GET.get('page', 1)
    paginator = Paginator(q_list, 3)
    try:
        q = paginator.page(page)
    except PageNotAnInteger:
        q = paginator.page(1)
    except EmptyPage:
        q = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'questions': q, 'tags': t_list})


def ask(request):
    t_list = Tags.objects.all().select_related()
    return render(request, 'ask.html', {'tags': t_list})


def login(request):
    t_list = Tags.objects.all().select_related()
    return render(request, 'login.html', {'tags': t_list})


def signup(request):
    t_list = Tags.objects.all().select_related()
    return render(request, 'signup.html', {'tags': t_list})


def one_question(request, pk):
    question = Question.objects.get(id=pk)
    t_list = Tags.objects.all().select_related()
    a_list = Answer.objects.all().select_related()

    return render(request, 'question.html', {"question": question, 'tags': t_list, "answers": a_list})


def hot(request):
    q_list = Question.objects.hot_questions()
    t_list = Tags.objects.all().select_related()
    page = request.GET.get('page', 1)
    paginator = Paginator(q_list, 3)
    try:
        q = paginator.page(page)
    except PageNotAnInteger:
        q = paginator.page(1)
    except EmptyPage:
        q = paginator.page(paginator.num_pages)

    return render(request, 'hot_questions.html', {'questions': q, 'tags': t_list})


def tag(request, title):
    t_list = Tags.objects.all().select_related()
    q_list = Question.objects.questions_by_tag(title)

    page = request.GET.get('page', 1)
    paginator = Paginator(q_list, 3)
    try:
        q = paginator.page(page)
    except PageNotAnInteger:
        q = paginator.page(1)
    except EmptyPage:
        q = paginator.page(paginator.num_pages)

    return render(request, 'tag_questions.html', {'questions': q, 'tags': t_list, 'title': title})
