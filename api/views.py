from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
import json

# Create your views here.

def auth(request, secret_key):
    print(secret_key)
    users = User.objects.filter(first_name=secret_key)
    ab = {}
    print(users.count())
    if users.count() > 0 :
        ab['is_auth'] = True
    else:
        ab['is_auth'] = False
    return HttpResponse("{}".format(json.dumps(ab)))

def add(request, qwe, asd):
    return HttpResponse("{} - {}".format(qwe, asd))