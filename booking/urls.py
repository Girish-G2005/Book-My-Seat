from django.urls import path
from .views import cancel_ticket, get_booked_seats, book_seat, ticket_details

urlpatterns = [
    path('get-booked-seats/', get_booked_seats, name = 'get-booked-seats'),
    path('book-seat/', book_seat, name = 'book-seat'),
    path('ticket/', ticket_details, name = 'ticket-details'),
    path('cancel/', cancel_ticket, name = 'cancel-booking'),
]