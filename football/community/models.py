from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Competition(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    caption = models.CharField(max_length=300)
    league = models.CharField(max_length=5)
    year = models.IntegerField(default=0)
    currentMatchday = models.IntegerField(default=0)
    numberOfMatchdays = models.IntegerField(default=0)
    numberOfTeams = models.IntegerField(default=0)
    numberOfGames = models.IntegerField(default=0)
    lastUpdated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ('caption', 'lastUpdated',)


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
    id = models.IntegerField(default=0, primary_key=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=25)
    matchday = models.IntegerField(default=0)
    homeTeamName = models.CharField(max_length=300)
    homeTeamId = models.IntegerField(default=0)
    awayTeamName = models.CharField(max_length=300)
    awayTeamId = models.IntegerField(default=0)
    goalsHomeTeam = models.IntegerField(default=0)
    goalsAwayTeam = models.IntegerField(default=0)
    # sourcelastupdated = models.CharField(max_length=15)
    createddate = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.matchday

    class Meta:
        ordering = ('matchday',)


class Profile(models.Model):
    # userid = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    # communities = models.ManyToManyField(Community)
    # isadmin = models.BooleanField()

    def __str__(self):
        return self.user.email

    class Meta:
        ordering = ('user',)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Group(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(Profile, through='Membership')
    games = models.ManyToManyField(Fixture, through='GroupFixture')
    createddate = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)
    # avatar = models.CharField(max_length=300)
    ispublic = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Membership(models.Model):
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    isadmin = models.BooleanField()

    def __str__(self):
        return self.group.name

    class Meta:
        ordering = ('date_joined',)


class GroupFixture(models.Model):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    fixtures = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group.name

    class Meta:
        ordering = ('createddate',)


class Prediction(models.Model):
    memberships = models.ForeignKey(Membership, on_delete=models.CASCADE)
    fixtures = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    awayteamgoals = models.IntegerField(default=0)
    hometeamgoals = models.IntegerField(default=0)
    iscorrect = models.BooleanField(default=False)
    createddate = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)


class Result(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
