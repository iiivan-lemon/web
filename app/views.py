from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import Question, Answer, Tags, User, Author, QuestionLikes, AnswerLikes


def index(request):
    q_list = Question.objects.new_questions()
    t_list = Tags.objects.all().select_related()[:6]
    q = paginate(request, q_list)
    u_list = User.objects.all().select_related()[:6]
    return render(request, 'index.html', {'page_obj': q, 'tags': t_list, 'users': u_list})


def ask(request):
    t_list = Tags.objects.all().select_related()[:6]
    u_list = User.objects.all().select_related()[:6]
    return render(request, 'ask.html', {'tags': t_list, 'users': u_list})


def login(request):
    t_list = Tags.objects.all().select_related()[:6]
    u_list = User.objects.all().select_related()[:6]
    return render(request, 'login.html', {'tags': t_list, 'users': u_list})


def signup(request):
    t_list = Tags.objects.all().select_related()[:6]
    u_list = User.objects.all().select_related()[:6]
    return render(request, 'signup.html', {'tags': t_list, 'users': u_list})


def set(request):
    t_list = Tags.objects.all().select_related()[:6]
    u_list = User.objects.all().select_related()[:6]
    return render(request, 'settings.html', {'tags': t_list, 'users': u_list})


def one_question(request, pk):
    question = Question.objects.get(id=pk)
    t_list = Tags.objects.all().select_related()[:6]
    u_list = User.objects.all().select_related()[:6]
    a_list = Answer.objects.answers_by_question(pk)

    a = paginate(request, a_list, 2)
    return render(request, 'question.html',
                  {"question": question, 'tags': t_list, "page_obj": a, 'users': u_list})


def hot(request):
    q_list = Question.objects.hot_questions()
    t_list = Tags.objects.all().select_related()[:6]
    u_list = User.objects.all().select_related()[:6]

    q = paginate(request, q_list)

    return render(request, 'hot_questions.html', {'page_obj': q, 'tags': t_list, 'users': u_list})


def tag(request, title):
    t_list = Tags.objects.all().select_related()[:6]
    u_list = User.objects.all().select_related()[:6]
    q_list = Question.objects.questions_by_tag(title)
    q = paginate(request, q_list)

    return render(request, 'tag_questions.html', {'page_obj': q, 'tags': t_list, 'title': title, 'users': u_list})


def paginate(request, objects_list, per_page=3):
    page = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj
