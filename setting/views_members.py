from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

from .forms import CreateUsersForm, AddGroupForm

def is_user_admin(user):
    return user.groups.filter(name='admin').exists()
# Create your views here.

@login_required
@user_passes_test(is_user_admin, login_url='dashboard_app:dashboard')
def members(request):
    users = User.objects.all()
    query = request.GET.get('q')
    form = CreateUsersForm()
    
    if request.method == 'POST':
        form = CreateUsersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('setting_app:members')

    if query:
        users = users.filter(Q(username__icontains=query) | Q(email__icontains=query))

    groups = Group.objects.all()
    
    return render(request, 'members.html', {'users': users, 'groups': groups,'form':form})

@login_required
@user_passes_test(is_user_admin, login_url='dashboard_app:dashboard')
def addmembers(request):
    
    if request.method == 'POST':
        form = CreateUsersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('setting_app:members')
    


@login_required
@user_passes_test(is_user_admin, login_url='dashboard_app:dashboard')
def delete_member(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()

    return redirect('setting_app:members')

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

@login_required
@user_passes_test(is_user_admin, login_url='dashboard_app:dashboard')
def edit_role(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            groups = form.cleaned_data['groups']
            user.groups.set(groups)
            
            return redirect('setting_app:members')
