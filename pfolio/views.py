from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf.urls import url


def index(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email =request.POST['message-email']
        message = request.POST['message']



        send_mail( "Contacted from - " + message_name,
                    message,
                    message_email,
                    ["sekar_vishaal@yahoo.co.in",]
                )


        messages.success(request, 'Thank You ' + message_name +' for sending email.I will contact you shortly.') # Any message you wish
        return HttpResponseRedirect("/")
    #    return render(request,"index.html", {'Message':message_name})'''
    else:
        return render(request,"index.html", {})
