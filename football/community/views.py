from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework import generics
from .models import Competition, Team, Fixture, Profile, Group, Membership, Prediction
from .serializers import CompetitionSerializer, GameSerializer, TeamSerializer, GroupSerializer
from .serializers import PredictionSerializer, MembershipSerializer, ProfileSerializer, UserSerializer
from django.contrib.auth.models import User

from django.views.generic.list import ListView
from django.utils import timezone

from .services import FootballData


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CompetitionList(generics.ListCreateAPIView):
    #FootballData.get_competitions()
    FootballData.get_games("445")
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class FixtureList(generics.ListCreateAPIView):
    queryset = Fixture.objects.all()
    serializer_class = GameSerializer


class FixtureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fixture.objects.all()
    serializer_class = GameSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MembershipList(generics.ListCreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class MembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class PredictionList(generics.ListCreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer


class PredictionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



