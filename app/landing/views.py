from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def landing_page(request):
    fs = FileSystemStorage()
    image_url = fs.url('kabosu.png')

    return render(request, "landing.html", {
        "image_url": image_url
    })
