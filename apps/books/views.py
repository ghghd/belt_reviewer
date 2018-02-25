from django.shortcuts import render, redirect
from .models import Book, Review
from ..users.models import User
from django.contrib import messages

def books(request):
    if request.session['loggedin'] != True:
        return redirect('users:index')
    else:
        context = {
            'user': User.objects.get(id = request.session['user']),
            'reviews': Review.objects.all().order_by('-id')[:3],
            'books': Book.objects.all()
        }
        return render(request, 'books/books.html', context)

def add(request):
    if request.session['loggedin'] != True:
        return redirect('users:index')
    else:
        context = {
            'lists': Book.objects.all()
        }
        return render(request, 'books/add.html', context)

def addprocess(request):
    book = Book.objects.addprocess(request.POST, request.session['user'])
    review = Review.objects.addprocess(request.POST, request.session['user'])
    bookid = book.id
    return redirect('books:book', book = bookid)

def book(request, book):
    if request.session['loggedin'] != True:
        return redirect('users:index')
    else:
        context = {
            'book': Book.objects.get(id = book),
            'reviews': Review.objects.filter(book = book)
        }
        request.session['book'] = book
        return render(request, 'books/book.html', context)

def reviewprocess(request):
    if Review.objects.filter(user = request.session['user'], book = request.session['book']):
        errors = Review.objects.reviewerror()
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags = tag)
        return redirect('books:book', book = request.session['book'])
    else:
        review = Review.objects.reviewprocess(request.POST, request.session['user'], request.session['book'])
        bookid = review.book.id
    return redirect('books:book', book = bookid)

def delete(request, review):
    review = Review.objects.delete(review)
    bookid = request.session['book']
    return redirect('books:book', book = bookid)

def user(request, user):
    if request.session['loggedin'] != True:
        return redirect('users:index')
    else:
        context = {
            'user': User.objects.get(id = user),
            'count': Review.objects.filter(user = user).count(),
            'books': Review.objects.filter(user = user)
        }
        return render(request, 'books/user.html', context)
