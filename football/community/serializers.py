
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Competition, Team, Fixture, Profile, Group, Membership, Prediction

class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

        
class FixtureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fixture
        fields = '__all__'




class UserSerializer(serializers.ModelSerializer):
   # profile = ProfileSerializer
    class Meta:
        model = User
        fields =('username', 'first_name','last_name', 'password','email') 

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('user','bio', 'location', 'birth_date',)

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created profile record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user,
                            bio=validated_data.pop('bio'), location=validated_data.pop('location'),
                            birth_date=validated_data.pop('birth_date'))
        return profile

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
    

        
class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prediction
        fields = '__all__'