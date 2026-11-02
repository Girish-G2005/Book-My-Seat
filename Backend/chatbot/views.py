from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import get_available_seat_count, get_jarvis_response, book_random_seat, cancel_booking
from .intents import Intent, get_intent

# API endpoint to handle chat messages and return the detected intent
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    message = request.data.get('message', '')

    if not message:
        return Response({'error': 'Message is required'}, status = status.HTTP_400_BAD_REQUEST)

    intent = get_intent(message)

    if intent == Intent.CHECK_AVAILABILITY:
        available_seats = get_available_seat_count()
        reply = available_seats['message']


    elif intent == Intent.BOOK_SEAT:
        result = book_random_seat(request.user)
        reply = result['message']

        if result['success']:
            reply += f"Your seat is at Table {result['table_no']} Seat {result['seat_no']}."


    elif intent == Intent.CANCEL_BOOKING:
        result = cancel_booking(request.user)
        reply = result['message']

    else:
        reply = get_jarvis_response(message)

    return Response({'reply': reply}, status = status.HTTP_200_OK)
