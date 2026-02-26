from django.shortcuts import render, redirect

# Create your views here.
from .models import ShortenedURL
from .forms import ShortenerForm
def index(request):
    if request.method == "POST":
        form = ShortenerForm(request.POST)
        if form.is_valid():
            # Save the new URL to the database
            form.save()
            return redirect('index')
    else:
        form = ShortenerForm()
    
    urls = ShortenedURL.objects.all().order_by('-created_at')
    return render(request, 'shortener/index.html', {'urls': urls, 'form': form})