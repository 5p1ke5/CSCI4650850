from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/users/login/")
def net_petz_list(request):
    pets = Pet.objects.filter(author=request.user).order_by('-date')
    return render(request, 'net_petz/net_petz_list.html', {'pets': pets})

@login_required(login_url="/users/login/")
def net_petz_page(request, slug):
    pet = Pet.objects.get(slug=slug)
    return render(request, 'net_petz/pet_page.html', {'pet': pet})

@login_required(login_url="/users/login/")
def feed_pet(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    pet.food += 1
    pet.save()
    return redirect('pets:page', slug=slug)


#@csrf_exempt  # optional in dev if form fails CSRF
@login_required(login_url="/users/login/")
def upload_pet_image(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    if request.method == 'POST' and request.FILES.get('image'):
        pet.image = request.FILES['image']
        pet.save()
    return redirect('pets:page', slug=slug)

@login_required(login_url="/users/login/")
def update_pet_name(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            pet.name = new_name
            pet.slug = slugify(new_name)
            pet.save()
            return redirect('pets:page', slug=pet.slug)
    return redirect('pets:page', slug=slug)


@login_required(login_url="/users/login/")
def create_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')

        if name:
            pet = Pet(name=name, slug=slugify(name))
            if image:
                pet.image = image
            if(request.user):
                pet.author = request.user
            pet.save()
            return redirect('pets:page', slug=pet.slug)

    return render(request, 'net_petz/create_pet.html')