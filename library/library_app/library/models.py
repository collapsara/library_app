from django.db import models
from django.db.models.fields.related import ForeignKey


class Genre(models.Model):
    name = models.CharField(verbose_name="genre_name", max_length=256, unique=True)


class Library(models.Model):
    name = models.CharField(verbose_name="library_name", max_length=256, unique=True)
    address = models.CharField(verbose_name="library_address", max_length=512)
    work_time = models.CharField(verbose_name="library_work_time", max_length=512)


class Book(models.Model):
    name = models.CharField(verbose_name="book_name", max_length=256, unique=True)
    year = models.CharField(verbose_name="book_year", max_length=512)
    autor = models.CharField(verbose_name="book_autor", max_length=512)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Autor(models.Model):
    fio = models.CharField(verbose_name="fio", max_length=256, unique=True)
    year = models.CharField(verbose_name="autor_year", max_length=512)


class Comment(models.Model):
    autor = models.CharField(verbose_name="fio", max_length=256, unique=True)
    book = models.ForeignKey(verbose_name="autor_year", max_length=512)
    create_date = models.DateTimeField(verbose_name="comment_create_date", auto_now_add=True)