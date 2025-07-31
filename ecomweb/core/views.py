from django.shortcuts import render
from .models import SuperCar
from .models import spcars
from .models import Brand

# Render an HTML template
# def home(request):
#     scars = SuperCar.objects.all()
#     return render(request, 'home.html',{scars:SuperCar})  # Make sure this template exists

def home(request):
    cars = SuperCar.objects.all()
    logos = Brand.objects.all()
    context = {
        'cars': cars,
        'logos': logos
    }
    return render(request, 'home.html', context)


def cart_view(request):
    cars = spcars.objects.all()  # Get all cars
    return render(request, 'cart.html', {'cars': cars})