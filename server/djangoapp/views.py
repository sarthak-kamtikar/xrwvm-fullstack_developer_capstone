import json
import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]

    user = authenticate(username=username, password=password)
    response_data = {"userName": username}

    if user is not None:
        login(request, user)
        response_data = {
            "userName": username,
            "status": "Authenticated",
        }

    return JsonResponse(response_data)


def logout_user(request):
    logout(request)
    return JsonResponse({"userName": ""})


@csrf_exempt
def registration(request):
    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "POST request required"},
            status=405,
        )

    try:
        data = json.loads(request.body)
        username = data["userName"]

        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"status": "error", "message": "Username already exists"},
                status=400,
            )

        User.objects.create_user(
            username=username,
            password=data["password"],
            first_name=data.get("firstName", ""),
            last_name=data.get("lastName", ""),
            email=data.get("email", ""),
        )

        return JsonResponse(
            {"userName": username, "status": "Registered"},
            status=201,
        )
    except (KeyError, json.JSONDecodeError):
        return JsonResponse(
            {"status": "error", "message": "Invalid registration data"},
            status=400,
        )