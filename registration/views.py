from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize


def index(request):
    return HttpResponse('<h1>Главная</h1>')


def reg(request):
    return HttpResponse('<h1>Регистрация</h1>')


def auth(request):
    # data = {
    #     'name': request.user.username,  # username of current logged-in user, otherwise Anonymous
    #     'url': 'https://www.pyscoop.com/',
    #     'skills': ['Python', 'Django'],
    # }
    # return JsonResponse(data)
    return HttpResponse('<h1>Аутентификация</h1>')


from .models import Users


class Users_View(Users):


    def get(self, request):
        # users_count = Users.objects.count()  # TOTAL books in the database
        users = Users.objects.all()  # Get all book objects from the database

        users_serialized_data = serialize('python', users)
        data = {
            # 'Users count': users_count,
            'users': users_serialized_data,
        }
        return JsonResponse(data)
