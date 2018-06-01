from django.conf.urls import url
from . import views

app_name='predictor'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home/$',views.home, name="home"),
    url(r'^login/$', views.login_users, name="login_users"),
    url(r'^register/$', views.register, name="register"),
    url(r'^pastdata/$', views.pastdata, name="pastdata"),
    url(r'^form/$', views.predictorform, name="predictorform"),
    url(r'^prediction/$', views.spillpredictor, name="spillpredictor"),
    url(r'^about/$', views.about, name="about"),
    url(r'^adddata/$', views.add_data, name="add_data"),


]
