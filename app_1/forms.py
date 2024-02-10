from django import forms
import datetime
from .models import Author,Post

# Задание 4_№1
# Доработаем задачу про броски монеты, игральной кости и# случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости,# числа.
# Второе поле предлагает указать количество попыток от 1 до 64.

class GameTypeForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('C', 'Coins'), ('D','Dice'), ('N','Numbers')])
    throws_number= forms.IntegerField(min_value=1, max_value=64)

# Задание 4_№3
# Продолжаем работу с авторами, статьями и комментариями.
# Создайте форму для добавления нового автора в базу # данных.
# Используйте ранее созданную модель Author

# class AuthorAddForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     bio = forms.CharField()
#     birthday = forms.DateField(initial=datetime.date.today)

class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','last_name','email','bio','birthday']

# Задание 4_№4
# Аналогично автору создайте форму добавления новой статьи.
# Автор статьи должен выбираться из списка (все доступные в  базе данных авторы).
class PostAddFormVidjet(forms.Form):
    title = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите заголовок статьи'}))
    content = forms.CharField(max_length=150,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите текст статьи'}))
    publish_date = forms.DateTimeField(initial=datetime.datetime.now,
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Введите категорию статьи'}))

    # views = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_published = forms.BooleanField(required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

# Задание 4_№5
#  Доработаем задачу 6 из прошлого семинара.
#  Мы сделали вывод статьи и комментариев.
#  Добавьте форму ввода нового комментария в существующий шаблон

