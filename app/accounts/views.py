from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import render, HttpResponseRedirect, Http404,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib import messages
from django.conf.urls import url
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST[ 'first_name' ]
        last_name = request.POST[ 'last_name' ]
        username = request.POST[ 'username' ]
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:

            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            

            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('register')

            user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            user.save();
         
            return redirect('login')

        else:
            messages.info(request,'Password not match')
            return redirect('register')

    else:

        context = locals()

        return render(request,'register.html',context)


def login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:

        context = locals()

        return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('index')