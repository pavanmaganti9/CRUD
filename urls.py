from django.conf.urls import url,include
from django.contrib import admin
from .import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^new/$', views.post_create, name='post_create'),
	url(r'^data/$', views.data, name='data'),
	url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
	url(r'^update/(?P<pk>\d+)$', views.update, name='update'),
	url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
	url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
]
