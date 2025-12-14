from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os


def home_view(request):
    """Домашняя страница со списком доступных страниц"""
    pages = [
        {'name': 'Текущее время', 'url': '/current_time/'},
        {'name': 'Рабочая директория', 'url': '/workdir/'},
    ]
    return render(request, 'home.html', {'pages': pages})


def current_time(request):
    """Показывает текущее время"""
    now = datetime.now()
    time_str = now.strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f'<h1>Текущее время: {time_str}</h1>')


def workdir(request):
    """Выводит содержимое рабочей директории"""
    files = os.listdir('.')
    files_list = '<br>'.join(files)
    return HttpResponse(f'<h1>Содержимое рабочей директории:</h1><p>{files_list}</p>')

