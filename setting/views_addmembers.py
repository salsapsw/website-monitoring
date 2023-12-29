# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required, user_passes_test
# from .forms import CreateUsersForm

# def is_user_admin(user):
#     return user.groups.filter(name='admin').exists()

# @login_required
# @user_passes_test(is_user_admin, login_url='dashboard_app:dashboard')
# def addmembers(request):
#     # Periksa apakah pengguna adalah admin sebelum menangani formulir
#     if not is_user_admin(request.user):
#         return redirect('dashboard_app:dashboard')

#     form = CreateUsersForm()

#     if request.method == 'POST':
#         form = CreateUsersForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('setting_app:members')

#     context = {'form': form}
#     return render(request, 'members.html', context)

from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CreateUsersForm, AddGroupForm

def is_user_admin(user):
    return user.groups.filter(name='admin').exists()

@login_required
@user_passes_test(is_user_admin, login_url='dashboard_app:dashboard')
def addmembers(request):
    if not is_user_admin(request.user):
        return redirect('dashboard_app:dashboard')

    form = CreateUsersForm()

    if request.method == 'POST':
        form = CreateUsersForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Member successfully added.')
            return redirect('setting_app:members')
        else:
            messages.error(request, 'Failed to add member. Please check the form for errors.')

    context = {'form': form}
    return render(request, 'members.html', context)

@login_required
@user_passes_test(is_user_admin, login_url='dashboard_app:dashboard')
def add_group(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = AddGroupForm()

    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            groups = form.cleaned_data['groups']
            user.groups.set(groups)

            return redirect('setting_app:members')

    return render(request, 'add_group.html', {'form': form, 'user': user})

# # Send email with login information
            # subject = 'Your Account Has Been Created'
            # message = f'Congratulations, your account has been successfully created!\n\nUsername: {User.username}\nPassword: {form.cleaned_data["password1"]}'
            # from_email = 'noreply.pmpd@gmail.com'
            # to_email = form.cleaned_data['email']

            # try:
            #     send_mail(subject, message, from_email, [to_email])
            #     messages.success(request, 'Member successfully added, and a notification email has been sent.')
            #     return redirect('setting_app:members')
            # except BadHeaderError:
            #     messages.error(request, 'Error occurred during email sending. Please check the email content.')
            # except ValidationError as e:
            #     messages.error(request, f'Validation error: {e}')
            # except Exception as e:
            #     messages.error(request, f'An error occurred during email sending: {str(e)}')
