from django.shortcuts import render

# Create your views here.
from .models import ShortenedURL
def index(request):
    # This will eventually show our list of URLs
    urls = ShortenedURL.objects.all()
    return render(request, 'shortener/index.html', {'urls': urls})