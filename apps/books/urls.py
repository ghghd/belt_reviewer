from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'books$', views.books, name = 'books'),
    url(r'books/add$', views.add, name = 'add'),
    url(r'books/addprocess$', views.addprocess, name = 'addprocess'),
    url(r'books/(?P<book>\d+)$', views.book, name = 'book'),
    url(r'books/reviewprocess$', views.reviewprocess, name = 'reviewprocess'),
    url(r'books/delete/(?P<review>\d+)$', views.delete, name = 'delete'),
    url(r'user/(?P<user>\d+)', views.user, name = 'user')
]
