from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import AddVideoForm


def videos(request):
    return render(request, 'videos/videos.html')


@login_required
def add_video(request):
    if request.method == 'POST':
        form = AddVideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('videos'))
    else:
        form = AddVideoForm()
    context = {
        'form': form,
    }
    return render(request, 'videos/add_video.html', context)
