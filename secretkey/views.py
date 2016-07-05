from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.models import User
import hashlib
# Create your views here.

def getit(request):
    current_user = auth.get_user(request)
    user_name = current_user.username
    user = User.objects.filter(username=user_name)
    m = hashlib.new('md5')
    m.update(user_name.encode('utf-8'))
    hex_hash = m.hexdigest()[:10]
    user_object = User.objects.filter(username=current_user.username)
    for item in user_object:
        item.first_name = hex_hash[:10]
        item.save()
    return render(request, 'secretkey/getit.html', {'hex_hash': hex_hash})