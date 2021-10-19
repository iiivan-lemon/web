from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

questions = [
    {
        'id': idx,
        'title': f'QUESTION {idx}',
        'text': f'Lorem ipsum dolor sit amet, consectetur adipisicing elit  tempor incididunt ut labore et dolore '
                f'magna aliqua. Ut enim ad minim veniam, '
                f'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo'
                f'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse'
                f'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non'
                f'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    } for idx in range(5)
]
hot_questions = [
    {
        'id': idx,
        'title': f'QUESTION {idx}',
        'text': f'Lorem ipsum dolor sit amet, consectetur adipisicing elit  tempor incididunt ut labore et dolore '
                f'magna aliqua. Ut enim ad minim veniam, '
                f'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo'
                f'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse'
                f'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non'
                f'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    } for idx in range(3)
]


def index(request):
    user_list = questions
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        q = paginator.page(page)
    except PageNotAnInteger:
        q = paginator.page(1)
    except EmptyPage:
        q = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'questions': q})


def ask(request):
    return render(request, 'ask.html', {})


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def one_question(request, pk):
    question = questions[pk]
    return render(request, 'question.html', {"question": question})


def hot(request):
    user_list = hot_questions
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        hot_q = paginator.page(page)
    except PageNotAnInteger:
        hot_q = paginator.page(1)
    except EmptyPage:
        hot_q = paginator.page(paginator.num_pages)

    return render(request, 'hot_questions.html', {'hot_questions': hot_q})
