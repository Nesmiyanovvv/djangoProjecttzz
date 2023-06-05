from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import Memory

def main(request):
    return render(request, 'main.html')


def profile(request):
    return render(request, 'memories.html.html')


def memories(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        title = request.POST.get('title')
        comment = request.POST.get('comment')

        # Здесь вы можете выполнить дополнительные действия для сохранения данных,
        # например, создать модель и сохранить данные в базе данных.

        # Пример вывода введенных данных в консоль:
        print("Место на карте:", location)
        print("Название:", title)
        print("Комментарий:", comment)

        memory = Memory(location=location, title=title, comment=comment)
        memory.save()

        # Очистить форму
        return render(request, 'memories_save.html')
    else:
        memories = Memory.objects.all()
        count = memories.count()
        context = {'memories': memories, 'count': count}

    return render(request, 'memories.html', context)


def memories_save(request):
    return render(request, 'memories_save.html')