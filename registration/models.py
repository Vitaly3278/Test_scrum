from django.db import models

class Users(models.Model):
    e_mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.e_mail



# Перейти в консоль python .\manage.py shell
# импортировать модуль from registration.models import Users
#
# Создать запись Users.objects.create(e_mail = e_mail, password = password)
#
# Получать все e-mail из таблицы (Users.objects.all())
# по индексу:  w =  Users.objects.all()      w[1].e_mail первая запись
#
#
# Изменение данных таблицы
# s = Users.objects.get(pk=1)
# s.password = '12345'
# s.save()
#
# УДАЛИТЬ ЗАПИСЬ
# Users.objects.filter(e_mail = 'django@mail.ru').delete()
