from django.db import models

class SuperCar(models.Model):
    CAR_TYPE_CHOICES = [
        ('SUV', 'SUV'),
        ('luxurySUVs','luxurySUVs'),
        ('Sedan', 'Sedan'),
        ('Coupe', 'Coupe'),
        ('Hatchback', 'Hatchback'),
        ('Convertible', 'Convertible'),
        ('Electric', 'Electric'),
        ('Truck', 'Truck'),
        ('Other', 'Other'),
    ]

    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used', 'Used'),
    ]

    car_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    running_kilometers = models.PositiveIntegerField()
    vehicle_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    model_year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20, default='Petrol')  # Petrol, Diesel, Electric, etc.
    transmission = models.CharField(max_length=20, default='Automatic')  # Manual, Automatic
    color = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='supercars/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand_name} {self.car_name} ({self.model_year})"


class spcars(models.Model):
    image=models.ImageField(upload_to='car-img/')
    name=models.CharField(max_length=50)
    brands=models.CharField(max_length=50)
    carprice=models.IntegerField()
    km=models.IntegerField()
    car_year=models.IntegerField()
    car_typ=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} ({self.brands})"
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos/')

    def __str__(self):
        return self.name