from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ProfileForm
from .models import Profile
from django.contrib import messages


def register(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.data.get("username")
			password = form.data.get("password1")
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
			return redirect("login_page")

	return render(request, "users/register.html", {"form" : form})


def profile_page(request):
	profile = Profile.objects.get(id=request.user.id)
	return render(request, "users/profile.html", {"profile" : profile})


def profile_update(request):

	id_ = request.user.id
	user_profile = get_object_or_404(Profile, id=id_)
	form = ProfileForm(instance=user_profile)

	if request.method == "POST":
		form = ProfileForm(request.POST, instance=user_profile)
		if form.is_valid():
			form.save()

	if request.FILES.get('image', None) != None:
		print(request.FILES)
		user_profile.image = request.FILES['image']
		user_profile.save()
		messages.success(request, 'Profile was updated successfully!')
		return redirect('ProfilePage')
	return render(request, "users/profile_update.html", {'form': form})
