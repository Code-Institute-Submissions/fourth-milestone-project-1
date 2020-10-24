from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import AddVideoForm


def videos(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'videos/videos.html', context)


@login_required
def add_video(request):
    if not request.user.is_superuser:
        return redirect(reverse('videos'))
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


@login_required
def edit_video(request, id):
    if not request.user.is_superuser:
        return redirect(reverse('videos'))
    video = get_object_or_404(Video, id=id)
    if request.method == 'POST':
        form = AddVideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect(reverse('videos'))
    else:
        form = AddVideoForm(instance=video)
    context = {
        'form': form,
        'video': video,
    }
    return render(request, 'videos/edit_video.html', context)


@login_required
def delete_video(request, id):
    if not request.user.is_superuser:
        return redirect(reverse('videos'))
    video = get_object_or_404(Video, id=id)
    video.delete()
    return redirect(reverse('videos'))
