from django.conf.urls import url

from api import views

app_name = "api"

urlpatterns = [
    url(r"^auth/(?P<secret_key>\w+)$", views.auth, name='auth'),
    url(r"^(?P<secret_key>[\w-]+)/list/$", views.list, name='list'),
    url(r"^(?P<secret_key>[\w-]+)/delete/(?P<post_id>[\w-]+)/$", views.delete, name='delete'),
    url(r"^(?P<secret_key>[\w-]+)/add/(?P<title>[\w-]+)/(?P<text>[\w-]+)/$", views.add, name='add'),
]