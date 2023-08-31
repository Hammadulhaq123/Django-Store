from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    title = "Ecommerce Home Page"
    return render(request, "home/index.html", context={"title": title})


def categories(request):
    card = [
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 76.00,
        },
        {
            "src": "https://images.unsplash.com/photo-1622519407650-3df9883f76a5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVuJTIwZmFzaGlvbnxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=400&q=60",
            "category": "MEN",
            "title": "Casual Shirts",
            "price": 16.00,
        },
    ]
    title = "Ecommerce Categories"
    return render(
        request, "categories/index.html", context={"card": card, "title": title}
    )
