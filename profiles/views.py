from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


@login_required
def profile(request):
    # Your logic to retrieve and pass user profile data here
    return render(request, 'profile.html')


@login_required
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user.customuser)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user.customuser)
    return render(request, 'profile_update.html', {'form': form})
