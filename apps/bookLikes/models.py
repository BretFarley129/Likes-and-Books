# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first = models.CharField(max_length = 255)
    last = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "User: \n{}\n{}\n{}\n{}\n".format(self.id, self.first, self.last, self.email)
    
    def __str__(self):
        return "Books in User: {}".format(self.books.all())

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(User, related_name = "books")
    liked_by = models.ManyToManyField(User, related_name = "liked_books")
    def __repr__(self):
        return "Book obj:\n{}\n{}\n".format(self.name, self.desc)