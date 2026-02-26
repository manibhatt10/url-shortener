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

from django.shortcuts import get_object_or_404

def redirect_url(request, short_code):
    # Find the URL object or return a 404 error if it doesn't exist
    url_instance = get_object_or_404(ShortenedURL, short_code=short_code)
    
    # Increment the click counter
    url_instance.clicks += 1
    url_instance.save()
    
    # Redirect to the original long URL
    return redirect(url_instance.original_url)