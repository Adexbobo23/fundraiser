from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UserProfileForm
from django.contrib import messages
from.models import UserProfile

# Create your views here.
def signin(request):
    if request.method == "POST": 
      username = request.POST['email']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None: 
        login(request, user)
        return redirect('home')
      else: 
        return render(request, 'signin.html', {'error': 'Invalid credentials.'})
    else: 
      return render(request, 'signin.html', {})


def logout_user(request): 
  logout(request)
  return redirect('home')


def signup(request):
    if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
        user = form.save()
        if user is not None:  
          login(request, user)
          messages.success(request, 'Account created successfully!')
          return redirect('home')
        else: 
           messages.error(request, 'Error creating account')
    else:
      form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user_profile = form.save(commit=False)

            # Keep the old avatar if no new image is uploaded
            if 'avatar' not in request.FILES and profile is not None:
                user_profile.avatar = profile.avatar

            # Create a new profile if it doesn't exist
            if profile is None:
                user_profile.user = request.user

            user_profile.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('home')
        else:
            # Log form errors to debug issues
            print("Form errors:", form.errors)  # Log in the console
            messages.error(request, "There were errors in your form. Please fix them.")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'user-profile.html',{'form':form})