from django.contrib import admin
from .models import Competition, Team, Fixture, Member, Community

# Register your models here.

admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Community)
admin.site.register(Member)