import ollama
from booking.models import CurrentBookings
from django.db import transaction, IntegrityError
import random


def get_jarvis_response(message):

    response = ollama.chat(
        model = "jarvis:latest",
        messages = [
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a polite, friendly, and helpful seat-booking assistant. "

                    "Your responsibilities are strictly limited to checking seat availability, "
                    "booking a random available seat, and cancelling the user's current booking. "

                    "Respond naturally to basic greetings and casual small talk. "
                    "Always maintain a warm, respectful, and welcoming tone. "

                    "If users ask unrelated questions or request things outside your capabilities, "
                    "politely explain that you are designed specifically for seat-booking assistance. "
                    "Never sound rude, dismissive, sarcastic, or annoyed. "

                    "Keep responses short, natural, and conversational. "

                    "IMPORTANT RULES: "
                    "Never invent or guess the number of available or occupied seats. "
                    "Only report seat availability using actual data provided by the backend. "
                    "Never claim that a seat has been booked or a booking has been cancelled "
                    "unless the backend explicitly confirms the operation. "
                    "Never assume that an operation was successful. "
                    "If backend information is unavailable, politely inform the user "
                    "that you cannot verify the information at the moment. "
                )
            },
            {
                "role": "user",
                "content": message
            }
        ],
        think = False
    )

    return response.message.content


# To get the available seat count
TOTAL_SEATS = 36

def get_available_seat_count():
    booked_count = CurrentBookings.objects.count()
    return {
        'message': f'There are {TOTAL_SEATS - booked_count} seats available out of {TOTAL_SEATS}.',
    }


# To book a random seat

TOTAL_TABLES = 6
TOTAL_SEATS_PER_TABLE = 6

def book_random_seat(user):
    try:
        with transaction.atomic():
            # Check if the user already has a booking
            if CurrentBookings.objects.filter(user = user).exists():
                return {'success': False, 
                        'message': 'You have already booked a seat.'}

            # Get the list of all booked seats
            booked_seats = set( CurrentBookings.objects.values_list('table_no', 'seat_no') )

            # Generate a list of all possible seats
            available_seats = [
                (table_no, seat_no)
                for table_no in range(1, TOTAL_TABLES + 1)
                for seat_no in range(1, TOTAL_SEATS_PER_TABLE + 1)
                if (table_no, seat_no) not in booked_seats
            ]

            if not available_seats:
                return {
                    'success': False,
                    'message': 'No seats are available for booking at the moment.'
                }

            # Select a random available seat
            table_no, seat_no = random.choice(available_seats)

            # Create a new booking for the user
            CurrentBookings.objects.create(user = user, table_no = table_no, seat_no = seat_no)

            return {
                'success': True,
                'message': 'Seat booked successfully.',
                'table_no': table_no,
                'seat_no': seat_no
            }

    except IntegrityError:
        return {
            'success': False,
            'message': 'An error occured while booking the seat. Please try again.'
        }


def cancel_booking(user):
    booking = CurrentBookings.objects.filter(user = user).first()

    if booking is None:
        return {
            'success': False,
            'message': 'You do not have any seat booked to cancel.'
        }

    booking.delete()

    return {
        'success': True,
        'message': 'Your booking has been cancelled successfully.'
    }
