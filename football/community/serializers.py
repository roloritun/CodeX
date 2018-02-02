from rest_framework import serializers
from .models import Competition, Team, Fixture, Member, Community

class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
