from django.contrib import admin
from .models import Competition, Team, Fixture, Person, Group, Membership, Prediction

# Register your models here.

admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Group)
admin.site.register(Person)