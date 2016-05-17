from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class Author(models.Model):

    """

    """
    owner = models.ForeignKey('auth.User', related_name='Author')
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')


    def __unicode__(self):
        
        return "{0} {1}".format(self.first_name, self.last_name)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class Book(models.Model):
    """
    Book serializer
    """

    author = models.ForeignKey(Author, related_name='books')
    title = models.CharField(max_length=200,verbose_name='Book Title')
    isbn = models.CharField(max_length=200, verbose_name='ISBN')

    def __unicode__(self):
        return self.title
######


