from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropertyForm
from .models import Property

# Create your views here.
def homepage(request):
    return render(request, 'homepage/homepage.html')

def clients(request):
    return render(request, 'clients/clients.html')

def calendar(request):
    return render(request, 'calendar/calendar.html')

def profile(request):
    return render(request, 'profile/profile.html')

### Pages gestion des biens ###

def properties(request):
    # Page pour l'affichage et la gestion des biens (modification, suppression)
    properties = Property.objects.all()
    return render(request, 'properties/properties.html', {'properties': properties})

def add_property(request):
    # Page contenant un formulaire permettant d'ajouter un bien
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_property')  # Redirige vers la même page
    else:
        form = PropertyForm()
    
    properties = Property.objects.all()
    return render(request, 'properties/add_property.html', {
        'form': form,
        'properties': properties
    })

def delete_property(request, property_id):
    # Suppression d'un bien
    property = get_object_or_404(Property, id=property_id)
    property.delete()
    return redirect('properties')

def update_property(request, property_id):
    # Modification d'un bien
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('properties')  
    else:
        form = PropertyForm(instance=property)

    return render(request, 'properties/update_property.html', {'form': form})





