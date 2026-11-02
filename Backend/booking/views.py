from django.contrib.auth.models import User
from rest_framework import response
from .models import CurrentBookings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import CurrentBookingSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import transaction, IntegrityError



# Fetching the booked seats from the CurrentBookings model to display the available seats on UI
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_booked_seats(request):

    bookedSeats = CurrentBookings.objects.all()
    bookedSerializer = CurrentBookingSerializer(bookedSeats, many=True)
    return Response(bookedSerializer.data, status = status.HTTP_200_OK)



# Booking a seat the user has requested. The user must be authenticated for the seat
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_seat(request):

    table_no = request.data.get('table_no')
    seat_no = request.data.get('seat_no')

    # validating the input data
    if table_no is None or seat_no is None:
        return Response({'error': 'Table number and Seat number are required.'}, status = status.HTTP_400_BAD_REQUEST)

    if not str(table_no).isdigit() or not str(seat_no).isdigit():
        return Response({'error': 'Table number and seat number must be integers.'}, status = status.HTTP_400_BAD_REQUEST)

    table_no = int(table_no)
    seat_no = int(seat_no)

    if (table_no <= 0 or seat_no <= 0):
        return Response({'error': 'Table number and Seat number should be positive numbers.'}, status = status.HTTP_400_BAD_REQUEST)

    try:
        with transaction.atomic():

            # Checking whether user has already booked a seat
            if CurrentBookings.objects.filter(user = request.user).exists():
                return Response({'error': 'You already booked a seat.'}, status = status.HTTP_400_BAD_REQUEST)

            # Checking whether the seat is already booked
            if CurrentBookings.objects.filter(table_no = table_no, seat_no = seat_no).exists():
                return Response({'error': 'This seat has already been booked by another user.'}, status = status.HTTP_400_BAD_REQUEST)

            # booking the seat
            CurrentBookings.objects.create(user = request.user, table_no = table_no, seat_no = seat_no)

            
    except IntegrityError:
        return Response({'error': 'Booking error occured. Either you already booked a seat or the seat was just booked.'}, status = status.HTTP_409_CONFLICT)

    return Response({'message': 'Seat booked successfully.'}, status = status.HTTP_201_CREATED)


# Fetching the user's table and seat details
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ticket_details(request):
    try:
        ticket = CurrentBookings.objects.get(user = request.user)

        return Response({"table_no": ticket.table_no,
                         "seat_no": ticket.seat_no,
                         "booked_at": ticket.booked_at}, status = status.HTTP_200_OK)
    except CurrentBookings.DoesNotExist:
        return Response({'error': 'No booking found.'}, status = status.HTTP_404_NOT_FOUND)


# Cancel a ticket
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cancel_ticket(request):
    try:
        ticket = CurrentBookings.objects.get(user = request.user)
        ticket.delete()

        return Response({'message': 'Seat got cancelled successfully.'}, status = status.HTTP_200_OK)
    except CurrentBookings.DoesNotExist:
        return Response({'error': 'No booking found to cancel.'}, status = status.HTTP_404_NOT_FOUND)
