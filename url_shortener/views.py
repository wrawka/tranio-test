from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F

from url_shortener.forms import UrlForm
from url_shortener.keygen import create_unique_random_key
from url_shortener.models import UserShortURL


def urls_index(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            key = create_unique_random_key()
            record = UserShortURL.objects.create(url=url, key=key)
            record.save()
            base_url = request.scheme + '://' + request.get_host() + request.get_full_path()
            return render(request, 'success.html', {'base_url': base_url, 'key': key})
    else:
        form = UrlForm()

    return render(request, 'index.html', {'form': form})


def short_url_redirect(request, key):
    record = get_object_or_404(UserShortURL, key=key)
    record.clicks = F('clicks') + 1
    record.save()
    return redirect(record.url)


def urls_stats(request):
    HEADERS = ['Slug', 'URL', 'Clicks', 'Created at']
    urls = UserShortURL.objects.all()

    return render(request, 'stats.html', {'urls': urls, 'headers': HEADERS})
