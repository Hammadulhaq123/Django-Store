from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    return render(request, "index.html")


def items_page(request):
    items = Ecommerce.objects.all()

    if request.GET.get("search"):
        items = items.filter(title__icontains=request.GET.get("search"))

    context = {"items": items}

    return render(request, "store.html", context)


def self_admin(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        tag = data.get("tag")
        rating = data.get("rating")
        price = data.get("price")
        image = request.FILES.get("image")

        Ecommerce.objects.create(
            title=title, tag=tag, rating=rating, price=price, image=image
        )
        return redirect("/self-admin")

    items = Ecommerce.objects.all()

    if request.GET.get("search"):
        items = items.filter(title__icontains=request.GET.get("search"))

    context = {"items": items}
    return render(request, "admin.html", context)


def delete_item(request, id):
    query = Ecommerce.objects.get(id=id)
    query.delete()
    return redirect("/self-admin")


def update_item(request, id):
    query = Ecommerce.objects.get(id=id)
    context = {"item": query}

    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        tag = data.get("tag")
        rating = data.get("rating")
        price = data.get("price")
        image = request.FILES.get("image")

        query.title = title
        query.tag = tag
        query.rating = rating
        query.price = price
        if image:
            query.image = image

        query.save()
        return redirect("/self-admin")

    return render(request, "update_item.html", context)
