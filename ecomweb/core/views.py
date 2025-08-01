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

# def newcars(request):
#     brand = request.GET.get('brand')
#     max_price = request.GET.get('max_price')
#     year = request.GET.get('year')

#     new_cars = SuperCar.objects.filter(vehicle_type='New')

#     if brand:
#         new_cars = new_cars.filter(brand_name__icontains=brand)
#     if max_price:
#         new_cars = new_cars.filter(price__lte=max_price)
#     if year:
#         new_cars = new_cars.filter(model_year__gte=year)

#     return render(request, 'new-cars.html', {'new_cars': new_cars})

def newcars(request):
    # Get query parameters
    brand = request.GET.get('brand')
    max_price = request.GET.get('max_price')
    year = request.GET.get('year')
    fuel = request.GET.get('fuel')
    transmission = request.GET.get('transmission')
    vehicle_type = request.GET.get('vehicle_type')
    color = request.GET.get('color')

    # Start with new cars only
    new_cars = SuperCar.objects.filter(condition='New')

    # Apply filters based on query params
    if brand:
        new_cars = new_cars.filter(brand_name__icontains=brand)

    if max_price:
        new_cars = new_cars.filter(price__lte=max_price)

    if year:
        new_cars = new_cars.filter(model_year__gte=year)

    if fuel:
        new_cars = new_cars.filter(fuel_type__iexact=fuel)

    if transmission:
        new_cars = new_cars.filter(transmission__iexact=transmission)

    if vehicle_type:
        new_cars = new_cars.filter(vehicle_type__iexact=vehicle_type)

    if color:
        new_cars = new_cars.filter(color__iexact=color)

    # Render template
    return render(request, 'new-cars.html', {
        'new_cars': new_cars,
        'filters': {
            'brand': brand,
            'max_price': max_price,
            'year': year,
            'fuel': fuel,
            'transmission': transmission,
            'vehicle_type': vehicle_type,
            'color': color,
        }
    })

def usedcar(request):
    # Get filter values from query parameters
    brand = request.GET.get('brand')
    max_price = request.GET.get('max_price')
    year = request.GET.get('year')
    fuel = request.GET.get('fuel')
    transmission = request.GET.get('transmission')
    vehicle_type = request.GET.get('vehicle_type')
    color = request.GET.get('color')
    
    # Initial queryset: Only used cars
    used_cars = SuperCar.objects.filter(condition='Used')
    
    # Apply filters if provided
    if brand:
        used_cars = used_cars.filter(brand_name__icontains=brand)
    if max_price:
        used_cars = used_cars.filter(price__lte=max_price)
    if year:
        used_cars = used_cars.filter(model_year__gte=year)
    if fuel:
        used_cars = used_cars.filter(fuel_type__iexact=fuel)
    if transmission:
        used_cars = used_cars.filter(transmission__iexact=transmission)
    if vehicle_type:
        used_cars = used_cars.filter(vehicle_type__iexact=vehicle_type)
    if color:
        used_cars = used_cars.filter(color__iexact=color)

    # Render the filtered list
    return render(request, 'used-car.html', {
        'used_cars': used_cars,
        'filters': {
            'brand': brand,
            'max_price': max_price,
            'year': year,
            'fuel': fuel,
            'transmission': transmission,
            'vehicle_type': vehicle_type,
            'color': color,
        }
    })