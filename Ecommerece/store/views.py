from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")


def items_page(request):
    return render(request, "store.html")


def self_admin(request):
    return render(request, "admin.html")
