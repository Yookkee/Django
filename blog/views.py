from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Entry
from django.contrib import auth


def index(request):
    latest_entry_list = Entry.objects.order_by('-pub_date')#[:10]
    context = {'latest_entry_list': latest_entry_list, 'username': auth.get_user(request).username}
    return render(request, 'blog/index.html', context)

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/detail.html', {'entry': entry, 'username': auth.get_user(request).username})