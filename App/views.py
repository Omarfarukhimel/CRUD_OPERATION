from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
import os


# Create your views here.
def home(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        print(search)
        if search:
            user_prof = Profile.objects.filter(Q(name__icontains=search) | Q(email__icontains=search))
            if not user_prof:
                messages.success(request, 'no such account exists')
                return redirect('home')
        else:
            user_prof = Profile.objects.all()
    return render(request, 'home.html', locals())


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        age = request.POST.get('age')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        if name:
            if image:
                prof = Profile.objects.create(
                    name=name,
                    image=image,
                    email=email,
                    age=age,
                    date_of_birth=date_of_birth,
                    phone_number=phone_number,
                    address=address,
                    gender=gender,
                    religion=religion,
                )
                prof.save()
                messages.success(request, 'profile updated.............')
                return redirect('home')
            else:
                prof = Profile.objects.create(
                    name=name,
                    email=email,
                    age=age,
                    date_of_birth=date_of_birth,
                    phone_number=phone_number,
                    address=address,
                    gender=gender,
                    religion=religion,
                )
                prof.save()
                messages.success(request, 'profile updated.............')
                return redirect('home')
        else:
            messages.error(request, 'please fill up all fields.....')

    return render(request, 'create.html', locals())


def delete(request, id):
    prof = Profile.objects.get(id=id)
    if prof.image.name != 'default_pic/def.png':
        # The image is not the default one, so we can safely delete it
        if os.path.exists(prof.image.path):
            os.remove(prof.image.path)
    prof.delete()
    return redirect('home')


def see_profile(request, id):
    prof = Profile.objects.get(id=id)
    return render(request, 'see_profile.html', locals())


def update_profile(request, id):
    prof = Profile.objects.get(id=id)
    if request.method == 'POST':
        if request.FILES.get('image') != None:
            if prof.image != 'default/def.jpg':
                if os.path.exists(prof.image.path):
                    os.remove(prof.image.path)

            prof.name = request.POST['name']
            prof.image = request.FILES.get('image')
            prof.email = request.POST.get('email')
            prof.age = request.POST.get('age')
            prof.address = request.POST.get('address')
            prof.phone_number = request.POST.get('phone_number')
            prof.date_of_birth = request.POST.get('date_of_birth')
            prof.religion = request.POST.get('religion')
            prof.gender = request.POST.get('gender')
            prof.save()
            messages.success(request, "Profile details Updated.")
            return redirect('home')
        else:
            prof.name = request.POST.get('name')
            prof.Email = request.POST.get('Email')
            prof.age = request.POST.get('age')
            prof.address = request.POST.get('address')
            prof.phone_number = request.POST.get('phone_number')
            prof.date_of_birth = request.POST.get('date_of_birth')
            prof.religion = request.POST.get('religion')
            prof.gender = request.POST.get('gender')
            prof.save()
            messages.success(request, "Profile details Updated.")
            return redirect('home')
    return render(request, 'update_profile.html', locals())
