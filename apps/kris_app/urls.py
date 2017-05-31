from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^form_process$', views.form_process),
  url(r'^dojo/create$', views.dojo_create),
  url(r'^user_id/(?P<id>\d+)$',views.user_id),
  url(r'^user_id/(?P<id>\d+)/edit$',views.user_id_edit),
  url(r'^user_id/(?P<id>\d+)/update$',views.user_id_update),

]