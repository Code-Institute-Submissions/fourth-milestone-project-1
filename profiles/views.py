from django.shortcuts import render


def user_profile(request):
    context = {}
    
    return render(request, 'profiles/profile.html', context)
