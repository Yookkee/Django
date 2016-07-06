from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
import json

# Create your views here.
from blog.models import Entry


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

def list(request, secret_key):
    users = User.objects.filter(first_name=secret_key)
    ab = {}
    if users.count() == 0:
        ab['result'] = "Unknown secret key"
        return HttpResponse("{}".format(json.dumps(ab)))
    else:
        user = users[0]

    entries = Entry.objects.filter(author=user)
    list = []
    for item in entries:
        entry = {}
        entry['title'] = item.title
        entry['text'] = item.text
        entry['id'] = item.id
        list.append(entry)

    ab['result'] = "ok"
    ab['list'] = list
    return HttpResponse("{}".format(json.dumps(ab)))