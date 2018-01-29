from django.utils import timezone
from django.db import models

import datetime
# Create your models here.

class Competition(models.Model):
    source_id = models.IntegerField(default=0)
    caption = models.CharField(max_length=300)
    league = models.CharField(max_length=5)
    year = models.CharField(max_length=4)
    numberofteams = models.IntegerField(default=0)
    numberofgames = models.IntegerField(default=0)
    sourcelastupdated = models.CharField(max_length=15)
    createddate = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ('caption',)

class Team(models.Model):
    source_id = models.IntegerField(default=0)
    name = models.CharField(max_length=300)
    shortname = models.CharField(max_length=5)
    sqaudmarketvalue = models.DecimalField(max_digits=18, decimal_places=2)
    createddate = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Fixture(models.Model):
    source_id  = models.IntegerField(default=0)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    fixturedate = models.DateTimeField()
    matchday = models.IntegerField(default=0)
    hometeamid = models.IntegerField(default=0)
    hometeamname = models.CharField(max_length=300)
    awayteamid = models.IntegerField(default=0)
    awayteamname = models.CharField(max_length=300)
    goalshometeam = models.IntegerField(default=0)
    goalsawayteam = models.IntegerField(default=0)
    sourcelastupdated = models.CharField(max_length=15)
    createddate = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.matchday

    class Meta:
        ordering = ('matchday',)


class Community(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    createddate = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)
    # avatar = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Member(models.Model):
    #userid = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email =  models.EmailField()
    password = models.CharField(max_length=100)
    communities = models.ManyToManyField(Community)
    isadmin = models.BooleanField()

    def __str__(self):
        return self.email

