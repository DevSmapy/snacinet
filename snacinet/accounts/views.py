from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from rest_framework import status

@api_view(["POST"])
def register_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    password_confirmation = request.data.get("password_confirmation")

    # 비밀번호 확인
    if password != password_confirmation:
        return Response({"Error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

    # 사용자 이름 중복 확인
    if User.objects.filter(username=username).exists():
        return Response({"Error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # 사용자 생성
    user = User.objects.create_user(username=username, password=password)
    user.save()

    return redirect('login_page')

@api_view(["POST"])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
    else:
        return Response({"Error": "Invalid credentials"}, status=400)

def main_view(request):
    return render(request, "main.html")

def login_page_view(request):
    return render(request, "login.html")

def register_page_view(request):
    return render(request, "register.html")