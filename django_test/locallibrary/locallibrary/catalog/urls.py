from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^allborrowed/$', views.BorrowedBooks.as_view(), name='all-borrowed'),

    url(r'^book/(?P<pk>\d+)$',
        login_required(views.BookDetailView.as_view()), name='book-detail'),

    url(r'^authors/$', login_required(views.AuthorListView.as_view()), name='authors'),

    url(r'^author/(?P<pk>\d+)$',
        login_required(views.AuthorDetailView.as_view()), name='author-detail'),

    url(r'^book/(?P<pk>[-\w]+)/renew/$',
        views.renew_book_librarian, name='renew-book-librarian'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
]
