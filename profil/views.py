# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash

# from .forms import UserEditForm

# @login_required
# def profil(request):
#     if request.method == 'POST':
#         # Form untuk mengubah password
#         password_form = PasswordChangeForm(request.user, request.POST, request.FILES)
#         if password_form.is_valid():
#             user = password_form.save()
#             update_session_auth_hash(request, user)  # Menghindari logout setelah mengubah password
#             messages.success(request, 'Password changed successfully!')
#         else:
#             messages.error(request, 'An error occurred in changing the password. Make sure the input is valid!')

#         # Form untuk mengedit informasi pengguna
#         user_edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
#         if user_edit_form.is_valid():
#             user_edit_form.save()
#             messages.success(request, 'Profile changed successfully!')
#         else:
#             messages.error(request, 'An error occurred in changing the profile. Make sure the input is valid!')

#         return redirect('profil_app:profil')
#     else:
#         password_form = PasswordChangeForm(request.user)
#         user_edit_form = UserEditForm(instance=request.user)

#     context = {
#         'password_form': password_form,
#         'user_edit_form': user_edit_form,
#     }
#     return render(request, 'profil.html', context)

# views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import UserEditForm, ProfilePictureForm, PasswordChangeCustomForm

@login_required
def profil(request):
    if request.method == 'POST':
        # Change password
        password_form = PasswordChangeCustomForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
        else:
            messages.error(request, 'An error occurred in changing the password. Make sure the input is valid!')

        # Change Profile
        user_edit_form = UserEditForm(request.POST, instance=request.user)
        profile_picture_form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)

        if user_edit_form.is_valid():
            user_edit_form.save()
            messages.success(request, 'Profile changed successfully!')
        else:
            messages.error(request, 'An error occurred in changing the profile. Make sure the input is valid!')

        if profile_picture_form.is_valid():
            profile_picture_form.save()
            messages.success(request, 'Profile picture changed successfully!')
        else:
            messages.error(request, 'An error occurred in changing the profile picture. Make sure the input is valid!')

        return redirect('profil_app:profil')
    else:
        password_form = PasswordChangeCustomForm(request.user)
        user_edit_form = UserEditForm(instance=request.user)
        profile_picture_form = ProfilePictureForm(instance=request.user)

    context = {
        'password_form': password_form,
        'user_edit_form': user_edit_form,
        'profile_picture_form': profile_picture_form,
    }
    return render(request, 'profil.html', context)
