from gc import get_objects

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.template.defaultfilters import title
from django.template.loader import render_to_string

from muslim.models import Women

menu = [
    {'title' : 'О сайте', 'url_name' : 'about'},
    {'title': 'Добавить статью', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title' : 'Анджелина Джоли', 'content': ' (англ. Angelina Jolie [7], при рождении Войт (англ. Voight), '
    'ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США)'
    ' — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер,'
    ' фотомодель, посол доброй воли ООН. Обладательница премии «Оскар», трёх премий «Золотой глобус» '
    '(первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США»',
     'is_published': True},
    {'id': 2, 'title' : 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': True},
    {'id': 3, 'title' : 'Эмили Стоун', 'content': 'Биография Эмили Стоун', 'is_published': True},
]

cats_db = [
    {'id' : 1, 'name' : 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]



def index(request):
    posts = Women.objects.filter(is_published=1)
    data = {
        'title': 'Главная Страница',
        'menu' : menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request,'muslim/index.html',context=data )

def about(request):
    return render(request,'muslim/about.html', {'title': 'О Сайте', 'menu': menu})

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug = post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request,'muslim/post.html', data)

def addpage (request):
    return HttpResponse("Добавления статьи")

def contact (request):
    return HttpResponse("Связаться с нами")

def login (request):
    return HttpResponse("Авторизация")

def show_category(request, cat_id):
    data = {
        'title': 'Отображения по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'muslim/index.html', context=data)

def addpage (request):
    return HttpResponse("Добавления статьи")

def page_not_found(request, exception):
    return HttpResponseNotFound(" <h1> Cтраница не найдена </h1>")