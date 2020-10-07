from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserOrderDetailsForm


@login_required
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    form = UserOrderDetailsForm(instance=user_profile)
    orders = user_profile.orders.all()
    context = {
        'user_profile': user_profile,
        'form': form,
        'orders': orders,
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def website_admin(request):
    return render(request, 'profiles/website_admin.html')
