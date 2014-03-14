from django.shortcuts import render, redirect

########## Views ##########


def landing(request):
    return render(request, 'landing.html')