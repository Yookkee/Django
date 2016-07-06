from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from django.utils import timezone

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

def delete(request, secret_key, post_id):
    users = User.objects.filter(first_name=secret_key)
    ab = {}
    if users.count() == 0:
        ab['result'] = "Incorrect query"
        return HttpResponse("{}".format(json.dumps(ab)))
    else:
        user = users[0]

    post = Entry.objects.filter(author=user).filter(id=post_id)
    ab = {}
    if post.count() == 0:
        ab['result'] = "Incorrect query"
        return HttpResponse("{}".format(json.dumps(ab)))
    else:
        ab['result'] = "Node deleted"
        post.delete()
        return HttpResponse("{}".format(json.dumps(ab)))

def add(request, secret_key, title, text):
    users = User.objects.filter(first_name=secret_key)
    ab = {}
    if users.count() == 0:
        ab['result'] = "Incorrect query"
        return HttpResponse("{}".format(json.dumps(ab)))
    else:
        user = users[0]

    pub_date = timezone.now()
    post = Entry(title=title, text=text, author=user, pub_date=pub_date)
    post.save()

    ab = {}
    ab['result'] = "New node created"
    return HttpResponse("{}".format(json.dumps(ab)))