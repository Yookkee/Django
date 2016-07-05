from django.conf.urls import url
from secretkey import views

app_name = "secretkey"
urlpatterns = [
    url(r'^$', views.getit, name='getit'),
]
