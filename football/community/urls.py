
from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^group/$', views.GroupList.as_view()),
   url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),
   url(r'^competition/$', views.CompetitionList.as_view()),
   url(r'^competition/(?P<pk>[0-9]+)/$', views.CompetitionDetail.as_view()),
   url(r'^team/$', views.TeamList.as_view()),
   url(r'^team/(?P<pk>[0-9]+)/$', views.TeamDetail.as_view()),
   url(r'^profile/$', views.ProfileList.as_view()),
   url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
   url(r'^fixture/$', views.FixtureList.as_view()),
   url(r'^fixture/(?P<pk>[0-9]+)/$', views.FixtureDetail.as_view()),
   url(r'^membership/$', views.MembershipList.as_view()),
   url(r'^membership/(?P<pk>[0-9]+)/$', views.MembershipDetail.as_view()),
   url(r'^prediction/$', views.PredictionList.as_view()),
   url(r'^prediction/(?P<pk>[0-9]+)/$', views.PredictionDetail.as_view()),
   url(r'^user/$', views.UserList.as_view()),
   url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
