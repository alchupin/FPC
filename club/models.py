from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    """Класс для описания Компании"""
    title = models.CharField(max_length=64, verbose_name='Наименование')
    site = models.CharField(max_length=128, verbose_name='Сайт компании')
    logo = models.ImageField()


class Member(models.Model):
    """Класс для описания участника КПЛ"""
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.CASCADE)
    about = models.TextField(verbose_name='О себе')
    interests = models.TextField(verbose_name='Интересы')
    movies = models.TextField(verbose_name='Любимые фильмы')
    books = models.TextField(verbose_name='Любимые книги')
    instagram = models.CharField(max_length=64, verbose_name='Страница в Инстаграм')
    facebook = models.CharField(max_length=64, verbose_name='Страница в Facebook')
    twitter = models.CharField(max_length=64, verbose_name='Страница Twitter')


class Idea(models.Model):
    """Класс для описания бизнес-идеи"""
    title = models.CharField(max_length=256, verbose_name='Заголовок идеи')
    text = models.TextField(verbose_name='Описание идеи')
    picture = models.ImageField()


class Event(models.Model):
    """Класс для описания мероприятия"""
    title = models.CharField(max_length=256, verbose_name='Заголовок мероприятия')
    text = models.TextField(verbose_name='Описание мероприятия')
    date = models.DateField(verbose_name='Дата мероприятия')
    picture = models.ImageField()


class Reference(models.Model):
    """Класс для описания рекомендуемой литературы"""
    title = models.CharField(max_length=256, verbose_name='Заголовок книги')
    text = models.TextField(verbose_name='Описание книги')
    picture = models.ImageField()


class News(models.Model):
    """Класс для описания новости"""
    title = models.CharField(max_length=256, verbose_name='Заголовок новости')
    text = models.TextField(verbose_name='Текст новости')
    date = models.DateField(verbose_name='Дата новости')
    picture = models.ImageField()
