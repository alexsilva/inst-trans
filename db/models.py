# coding: utf-8
from django.db import models

class Translation(models.Model):
    """
    source:
    target:
    sourceLocale:
    targetLocale:
    """
    source = models.CharField(max_length=255, unique=True)
    target = models.CharField(max_length=255)

    createdAt = models.DateTimeField(auto_now_add=True)

    sourceLocale = models.CharField(max_length=25)
    targetLocale = models.CharField(max_length=25)

    class Meta(object):
        app_label = "db"

    @property
    def simple(self):
        return [self.source, self.target]

    def __unicode__(self):
        return u"{0}: {1}".format(self.source, self.target)

class GrammaticalClass(models.Model):
    """
    name:
    words:
    """
    name = models.CharField(max_length=255)
    translation = models.ForeignKey("Translation")

    def __unicode__(self):
        return self.name

class Word(models.Model):
    """
    word:
    """
    name = models.CharField(max_length=255)
    grammaticalClass = models.ForeignKey("GrammaticalClass")

    def __unicode__(self):
        return self.name

class ReverseWord(models.Model):
    """
    reverse:
    """
    name = models.CharField(max_length=255)
    word = models.ForeignKey("Word")

    def __unicode__(self):
        return self.name