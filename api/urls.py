from django.conf.urls import url

from api import views

app_name = "api"

urlpatterns = [
    url(r"^auth/(?P<secret_key>\w+)$", views.auth, name='auth'),
    #url(r'^add(?P<qwe>\w+)-(?P<asd>\w+)$', views.add, name='add'),

]