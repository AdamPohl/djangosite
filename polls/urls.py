from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', 'polls.views.login'),
    url(r'^accounts/auth/$', 'polls.views.auth_view'),
    url(r'^accounts/logout/$', 'polls.views.logout'),
    url(r'^accounts/loggedin/$', 'polls.views.loggedin'),
    url(r'^accounts/new_user/$', 'polls.views.new_user'),
    url(r'^accounts/invalid/$', 'polls.views.invalid_login'),
    url(r'^accounts/make_new_user/$', 'polls.views.make_new_user'),
    url(r'^accounts/created_new_user/$', 'polls.views.cre_n_user'),

    url(r'^index/', 'polls.views.site_index'),

    url(r'^new_form/$', 'polls.views.new_form'),
    url(r'^make_form/$', 'polls.views.make_form'),
    url(r'^edit_form/$', 'polls.views.edit_form'),
    url(r'^read_only/(?P<pk>\d+)/$', views.webform_detail, name='webform_detail'),

    url(r'^new_quest/$', 'polls.views.new_quest'),
    url(r'^make_quest/$', 'polls.views.make_quest'),
]
