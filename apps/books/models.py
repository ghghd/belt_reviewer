from __future__ import unicode_literals
from django.db import models
from ..users.models import User

class BookManager(models.Manager):
    def addprocess(self, form, user):
        return self.create(title = form['title'], author = form['author'], user = User.objects.get(id = user))

class ReviewManager(models.Manager):
    def addprocess(self, form, user):
        return self.create(review = form['review'], rating = form['rating'], book = Book.objects.last(), user = User.objects.get(id = user))

    def reviewprocess(self, form, user, book):
        return self.create(review = form['review'], rating = form['rating'], book = Book.objects.get(id = book), user = User.objects.get(id = user))

    def reviewerror(self):
        errors = {}
        errors['error'] = "You may only add one review to each book."
        return errors

    def delete(self, review):
        Review.objects.get(id = review).delete()

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    user = models.ForeignKey(User, related_name = 'books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField(max_length = 1000)
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name = 'reviews')
    user = models.ForeignKey(User, related_name = 'reviews')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()
