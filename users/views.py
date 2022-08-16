from django.shortcuts import redirect, render
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from users.forms import ProfileUpdateForm, UserRegisterForm as UserCreationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "You profile has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(
        request, 
        'users/profile.html',
        {
            'u_form': u_form,
            'p_form': p_form,
        }
    )

def register(request):
    form = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! Now you can log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(
        request,
        'users/register.html',
        {
            'form': form
        }
    )