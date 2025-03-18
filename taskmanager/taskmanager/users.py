from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

# User Registration API
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "User registered successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)

# Token Generation (Using JWT)
@api_view(['POST'])
def get_tokens_for_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.filter(username=username).first()
    if user is None or not user.check_password(password):
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    })
