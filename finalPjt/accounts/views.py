from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm

from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm
from .models import Profile, User
from movies.models import Rating

from movies.models import Movie
import random


def login(request):
    num = random.randrange(1, 50)
    movie = Movie.objects.get(id=num)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # request, request.POST
        if form.is_valid():
            auth_login(request, form.get_user()) 
            return redirect(request.GET.get('next') or 'movies:list') 
    else: 
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'movie': movie})
    


def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    

def signup(request):
    if request.method == "POST":
        form =CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
        return redirect('movies:list')
    else:
        form = CustomUserCreationForm()
        
        return render(request, 'accounts/signup.html', {'form':form} )
        
        
def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people':people} )
    

def update(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(data=request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile) 
        
        if user_change_form.is_valid() and profile_form.is_valid(): 
            # 객체를 돌려줌
            user = user_change_form.save()
            
            profile = profile_form.save()
            print(profile.image.url)
            return redirect('people', user)
            
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        
        context = {
            'user_change_form': user_change_form,
            'profile_form': profile_form,
        }
        return render(request, 'accounts/update.html', context)
    
        
def delete(request):
    
    if request.method == "POST":
        request.user.delete()
        return redirect('accounts:signup')
        
    return render(request, 'accounts/delete.html')
    

def password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        
        if password_change_form.is_valid():
            # user = password_change_form.save()
            update_session_auth_hash(request, password_change_form)
        return redirect('people', request.user)
            
    else:
        password_change_form = PasswordChangeForm(request.user)
        return render(request, 'accounts/password.html', {'password_change_form':password_change_form})
        
def follow(request, user_id):
    # user_id = to user 즉, 내가 follow할 아이디
    person = get_object_or_404(get_user_model(), pk=user_id)
    
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)

    return redirect('people', person.username)
    
def mypage(request):
    ratings = Rating.objects.filter(user=request.user)
    return render(request, 'accounts/mypage.html', {'ratings':ratings})
    