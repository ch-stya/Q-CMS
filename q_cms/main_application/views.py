from django.shortcuts import render, redirect
from .forms import PropertyForm
from .models import Property

# Create your views here.
def homepage(request):
    return render(request, 'homepage/homepage.html')

def properties(request):
    properties = Property.objects.all()
    return render(request, 'properties/properties.html', {'properties': properties})

def clients(request):
    return render(request, 'clients/clients.html')

def calendar(request):
    return render(request, 'calendar/calendar.html')

def profile(request):
    return render(request, 'profile/profile.html')

def add_properties(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_properties')  # Redirige vers la même page
    else:
        form = PropertyForm()
    
    properties = Property.objects.all()
    return render(request, 'properties/add_properties.html', {
        'form': form,
        'properties': properties
    })
