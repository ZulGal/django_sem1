from django.db import models
# Задание №1
# 📌 Создайте модель для запоминания бросков монеты: орёл или решка.
# 📌 Также запоминайте время броска
# Задание №2
# 📌 Доработаем задачу 1.
# 📌 Добавьте статический метод для статистики по n последним  броскам монеты.
# 📌 Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
class Coin(models.Model):
    side = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add = True)
    # 28.10

    def __str__(self):
        return f'FellOut {self.side}, time: {self.time_created}'
    #     32.53

    @staticmethod
    def get_data(count):
        coints = Coin.objects.all()[:count]
        # [:count] срез
        coints_dict = {
            'орел':[],
            'решка':[]
        }
        # 51.36
        # print(coints)
        for i in coints:
            if i.side == 1:
                coints_dict['орел'].append(i.time_created)
            else:
                coints_dict['решка'].append(i.time_created)
        return coints_dict
#         57.30
# Задание №3
# 📌 Создайте модель Автор. Модель должна содержать
# следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное
# имя”, которое возвращает имя и фамилию

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Author: {self.name}, last_name: {self.last_name}, birthday: {self.birthday}'

    def full_name(self):
        return f'{self.name}, {self.last_name} '
#
# Создайте модель Статья (публикация). Авторы из прошлой задачи могут
# писать статьи. У статьи может быть только один автор. У статьи должны быть
# следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Post:{self.title}, Author: {self.author}'

