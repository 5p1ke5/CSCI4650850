from django.shortcuts import render
from .models import Pet

# Create your views here.
def net_petz_list(request):
    pets = Pet.objects.all().order_by('-date')
    return render(request, 'net_petz/net_petz_list.html', {'pets': pets})

def net_petz_page(request, slug):
    pet = Pet.objects.get(slug=slug)
    return render(request, 'net_petz/pet_page.html', {'pet': pet})
