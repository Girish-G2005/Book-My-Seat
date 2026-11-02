
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

# Create your views here.
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({'error': 'Username, password, and email are required.'}, status = status.HTTP_400_BAD_REQUEST)

    try:
        validate_email(email)
    except ValidationError:
        return Response({'error': 'Invalid email address.'}, status = status.HTTP_400_BAD_REQUEST)

    try:
        validate_password(password)
    except ValidationError as e:
        return Response({'error': e.messages}, status = status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username = username).exists():
        return Response({'error': 'Username already exists.'}, status = status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username = username, password = password, email = email)

    return Response({'message': 'User registered successfully.'}, status = status.HTTP_201_CREATED)

