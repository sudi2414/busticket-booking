from django.shortcuts import render, redirect
from .models import Bus_Booking
from .forms import Bus_Form

max_tickets = 10

def booking_success(request):
    return render(request, 'busticket/booking_sucess.html')

def ticket_booking(request):
    error = None
    if request.method == 'POST':
        form = Bus_Form(request.POST)
        if form.is_valid():
            from_city = form.cleaned_data['from_location'].lower()
            to_city = form.cleaned_data['to_location'].lower()
            journey_date = form.cleaned_data['journey_date']
            seats_book = form.cleaned_data['seats_booked']
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']

            # Find bus number from route mapping:
            bus_number = Bus_Booking.BUS_ROUTES.get((from_city, to_city))
            if not bus_number:
                error = 'No bus available for the selected route.'
            else:
                # Check seat availability
                bookings = Bus_Booking.objects.filter(bus_number=bus_number, journey_date=journey_date)
                total_booked = sum(booking.seats_booked for booking in bookings)
                seats_left = max_tickets - total_booked
                if seats_left < seats_book:
                    error = f'Only {seats_left} seats left on this bus for the selected date.'
                else:
                    Bus_Booking.objects.create(
                        from_location=from_city.upper(),
                        to_location=to_city.upper(),
                        journey_date=journey_date,
                        seats_booked=seats_book,
                        bus_number=bus_number,
                        name=name,
                        age=age
                    )
                    return redirect('booking_success')
        else:
            error = list(form.errors.values())[0][0]
    else:
        form = Bus_Form()

    return render(request, 'busticket/tickets.html', {
        'form': form,
        'error': error,
    })
