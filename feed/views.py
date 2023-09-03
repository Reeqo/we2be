from django.shortcuts import render
from feed.models import Video


def videos_list(request):
    sort = request.GET.get('sort')
    template = 'feed/feed.html'
    if sort == 'date:':
        videos = Video.objects.order_by('-published_at')
    elif sort == 'title':
        videos = Video.objects.order_by('title')
    else:
        videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, template, context)