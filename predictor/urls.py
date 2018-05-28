from django.conf.urls import url
from . import views



app_name='predictor'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.login_users, name="login_users"),
    url(r'^register/$', views.register, name="register"),
    url(r'^form/$', views.Prediction.spillPrediction, name="spillPrediction"),
]
