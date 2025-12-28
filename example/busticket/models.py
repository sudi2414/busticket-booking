from django.db import models

# Create your models here.
class Bus_Booking(models.Model):
    CHENNAI = 'chennai'
    HYDERABAD = 'hyderabad'
    BANGALORE = 'bangalore'
    COIMBATORE = 'coimbatore'
    MUMBAI = 'mumbai'
    DELHI = 'delhi'
    JAIPUR = 'jaipur'
    KOLKATA = 'kolkata'
    PONDICHERRY = 'pondicherry'
    VIJAYAWADA = 'vijayawada'
    MADURAI = 'madurai'
    GOA = 'goa'
    AGRA = 'agra'
    UDAIPUR = 'udaipur'
    DARJEELING = 'darjeeling'
    
    FROM_CHOICES = [
        ('CHENNAI', 'chennai'),
        ('HYDERABAD', 'hyderabad'),
        ('BANGALORE', 'bangalore'),
        ('COIMBATORE', 'coimbatore'),
        ('MUMBAI', 'mumbai'),
        ('DELHI', 'delhi'),
        ('JAIPUR', 'jaipur'),
        ('KOLKATA', 'kolkata'),
        ('PONDICHERRY', 'pondicherry')
    ]
    
    TO_CHOICES = [
        ('BANGALORE', 'bangalore'),
        ('VIJAYAWADA', 'vijayawada'),
        ('MADURAI', 'madurai'),
        ('GOA', 'goa'),
        ('AGRA', 'agra'),
        ('UDAIPUR', 'udaipur'),
        ('DARJEELING', 'darjeeling'),
        ('CHENNAI', 'chennai'),
        ('KOLKATA', 'kolkata'),
        ('PONDICHERRY', 'pondicherry'),
    ]
    BUS_ROUTES = {
        ('chennai', 'bangalore'): 'TN-01-2345',
        ('chennai', 'vijayawada'): 'TN-02-5678',
        ('chennai', 'madurai'): 'TN-03-8901',
        ('chennai', 'pondicherry'): 'TN-04-2341',
        ('hyderabad', 'bangalore'): 'TS-05-3456',
        ('hyderabad', 'vijayawada'): 'TS-06-6789',
        ('hyderabad', 'chennai'): 'TS-07-9012',
        ('bangalore', 'chennai'): 'KA-08-4567',
        ('bangalore', 'goa'): 'KA-09-7890',
        ('bangalore', 'hyderabad'): 'KA-10-0123',
        ('coimbatore', 'bangalore'): 'TN-11-5678',
        ('coimbatore', 'madurai'): 'TN-12-8901',
        ('coimbatore', 'chennai'): 'TN-13-1234',
        ('mumbai', 'goa'): 'MH-14-6789',
        ('mumbai', 'bangalore'): 'MH-15-9012',
        ('mumbai', 'agra'): 'MH-16-2345',
        ('delhi', 'agra'): 'DL-17-3456',
        ('delhi', 'jaipur'): 'DL-18-6789',
        ('delhi', 'udaipur'): 'DL-19-9012',
        ('jaipur', 'udaipur'): 'RJ-20-0123',
        ('jaipur', 'agra'): 'RJ-21-3456',
        ('jaipur', 'delhi'): 'RJ-22-6789',
        ('kolkata', 'darjeeling'): 'WB-23-7890',
        ('kolkata', 'bangalore'): 'WB-24-0123',
        ('kolkata', 'chennai'): 'WB-25-3456',
        ('pondicherry', 'chennai'): 'PY-26-4567',
        ('pondicherry', 'bangalore'): 'PY-27-7890',
        ('pondicherry', 'madurai'): 'PY-28-0123',
    }
    SEAT_CHOICES = [(i, str(i)) for i in range(1, 7)]

   
    
    from_location = models.CharField(max_length=50, choices=FROM_CHOICES)
    to_location = models.CharField(max_length=50, choices=TO_CHOICES)
    bus_number = models.CharField(max_length=50)
    booking_date = models.DateField(auto_now_add=True)
    journey_date = models.DateField()
    seats_booked = models.IntegerField(
    choices=SEAT_CHOICES,
    default=1
)    
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
    
