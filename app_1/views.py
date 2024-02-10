from django.shortcuts import render
import logging
from django.http import HttpResponse
from random import randint,choice
from .models import Coin, Author, Post
from .forms import GameTypeForm, AuthorAddForm, PostAddFormVidjet

logger = logging.getLogger(__name__)

# Задании 1 и 2 уроков:
# Задание 1_5
# Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# Орёл или решка
# Значение одной из шести граней игрального кубика
# Случайное число от 0 до 100
# Пропишите маршруты
def heads_or_tails(request):
    result = choice(['орел','решка'])
    if result == 'орел':
        res = 1
    else:
        res = 0
    logger.info(f'Выпало: {result}')
    coin = Coin(side=res)
    coin.save()
    my_dict = Coin.get_data(3)
    return HttpResponse(f'Монета показала: {result},{my_dict}')

def dice(request):
    dice_side = randint(1,6)
    logger.info(f'Dice side: {dice_side}')
    return HttpResponse(f'<p>Dice_side: {dice_side}</p>')

def digit(request):
    rand_number = randint(1,100)
    logger.info(f'Random number from 0 to 100: {rand_number}')
    return HttpResponse(f'<p>Random number from 0 to 100: {rand_number}</p>')

def authors_view(request):
    authors = Author.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])
    return HttpResponse(res_str)

def posts_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])
    return HttpResponse(res_str)

# Задание 3_1
# Изменяем задачу 8 из семинара 1 с выводом двух html страниц:
# главной и о себе.
# Перенесите вёрстку в шаблоны.
# Представления должны пробрасывать полезную информацию в
# шаблон через контекст.

# Задание 3_2
# Доработаем задачу 1.
# Выделите общий код шаблонов и создайте родительский шаблон base.html.
# Внесите правки в дочерние шаблоны.

def index(request):
    context = {
        'title': 'Главная страница',
    }
    logger.info('index get request')
    return render(request,template_name='app_1/index.html',context=context)

def about(request):
    context = {
        'title': 'Обо мне',
        'name': 'Алексей',
    }
    logger.info('about get request')
    return render(request,template_name='app_1/about.html',context=context)
# Задание 3_3
# Доработаем задачу 7 из урока 1, где бросали монетку,
# игральную кость и генерировали случайное число.
#  Маршруты могут принимать целое число - количество
# бросков.
#  Представления создают список с результатами бросков и
# передают его в контекст шаблона.
#  Необходимо создать универсальный шаблон для вывода
# результатов любого из трёх представлений.
def heads_or_tails3(request, count=3):
    list_result = []
    for i in range(count):
        list_result.append(choice(['орел','решка']))
    context = {
        'title': 'Орел или решка',
        'result': list_result,
    }
    return render(request, 'app_1/game.html',context=context)


def dice3(request, count):
    list_result = []
    for i in range(count):
        dice_side = randint(1, 6)
        logger.info(f'Dice side: {dice_side}')
        list_result.append(dice_side)
    context = {
        'title': 'Игральная кость',
        'result': list_result,
    }
    return render(request, 'app_1/game.html', context=context)

def digit3(request,count):
    list_result = []
    for i in range(count):
        rand_number = randint(1, 100)
        logger.info(f'Random number from 0 to 100: {rand_number}')
        list_result.append(rand_number)
    context = {
        'title': 'Случайное число',
        'result': list_result,
    }
    return render(request, 'app_1/game.html', context=context)

# Задание 3_4
# Доработаем задачи из прошлого семинара по созданию
# моделей автора, статьи и комментария.
# Создайте шаблон для вывода всех статей автора в виде
# списка заголовков.
# ○ Если статья опубликована, заголовок должен быть
# ссылкой на статью.
# ○ Если не опубликована, без ссылки.
# Не забываем про код представления с запросом к базе
# данных и маршруты


def author_post(request,author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)
    print(posts)
    context = {'author': author, 'posts':posts}
    return render (request,template_name='app_1/author_post.html', context=context)


def post_view(request,post_id):
    post = Post.objects.get(id=post_id)
    return render (request,template_name='app_1/post.html', context={'post':post})

# Задание 4_1
# Доработаем задачу про броски монеты, игральной кости и случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости, числа.
# Второе поле предлагает указать количество попыток от 1 до 64.

# Задание 4_№2
# Доработаем задачу 1. Создайте представление, которое выводит форму выбора.
# В зависимости от переданных значений представление вызывает одно из трёх представлений, созданных на
# прошлом семинаре (если данные прошли проверку, конечно же).

def choose_game(request):
    if request.method == 'POST':
        form = GameTypeForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            throws_number = form.cleaned_data['throws_number']
            logger.info(f'Получили {game_type=}, {throws_number=}')
            if game_type == 'C':
                return heads_or_tails3(request,throws_number)
            elif game_type == 'D':
                return dice3(request,throws_number)
            else:
                return digit3(request,throws_number)
    else:
        form = GameTypeForm()
    return render(request, 'app_1/games.html', {'form':form})


def author_add(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            logger.info(f'Получили {name=}, {last_name=}, {email=}, {bio=}, {birthday=}')
            author = Author(name=name, last_name=last_name, email=email, bio=bio, birthday=birthday)
            author.save()
            message = 'Автор сохранён'
    else:
        form = AuthorAddForm()
        message = 'Заполните форму'
    return render(request, 'app_1/author_form.html', {'form':form, 'message': message})


def post_add(request):
    if request.method == 'POST':
        form = PostAddFormVidjet(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            is_published = form.cleaned_data['is_published']
            logger.info(f'Получили {title=}, {content=}, {publish_date=}, {author=}, {category} {is_published}')
            post = Post(title=title, content=content, publish_date=publish_date, author=author, category=category, is_published=is_published)
            post.save()
            message = 'Пост сохранён'
    else:
        form = PostAddFormVidjet()
        message = 'Заполните форму'
    return render(request, 'app_1/post_form.html', {'form':form, 'message': message})