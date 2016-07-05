from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Entry
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.utils import timezone


def index(request):
    latest_entry_list = Entry.objects.order_by('-pub_date')#[:10]
    context = {'latest_entry_list': latest_entry_list, 'username': auth.get_user(request).username}
    return render(request, 'blog/index.html', context)

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/detail.html', {'entry': entry, 'username': auth.get_user(request).username})


def createpost(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')
        user = auth.get_user(request)
        if user.is_authenticated() is not None:
            args['createpost_error'] = "Login before creating posts!"
            return render_to_response("blog/createpost.html", args)
        elif title is None:
            args['createpost_error'] = "Write some title!"
            return render_to_response("blog/createpost.html", args)
        elif not text:
            args['createpost_error'] = "Write some text!"
            return render_to_response("blog/createpost.html", args)
        else:
            pub_date = timezone.now()
            post = Entry(title=title, text=text, author=user, pub_date=pub_date)
            post.save()
            return redirect('/');


    else:
        return render_to_response("blog/createpost.html", args)