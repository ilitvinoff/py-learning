from django.views import generic
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    # Метод 'all()' применен по умолчанию.
    num_authors = Author.objects.count()
    num_genres = Genre.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors, 'num_genres': num_genres},
    )


class BookListView(generic.ListView):
    model = Book
