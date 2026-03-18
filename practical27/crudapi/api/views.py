from django.http import JsonResponse
from .models import User
import json


# CREATE USER
def create_user(request):

    name = request.GET.get("name")
    email = request.GET.get("email")

    if name and email:
        user = User.objects.create(name=name, email=email)
        return JsonResponse({
            "message": "User created",
            "id": user.id
        })

    return JsonResponse({"message": "Provide name and email"})


# READ USERS
def get_users(request):

    users = list(User.objects.values())
    return JsonResponse(users, safe=False)


# UPDATE
def update_user(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        user = User.objects.get(id=id)
        user.name = data["name"]
        user.email = data["email"]
        user.save()
        return JsonResponse({"message": "User updated"})


# DELETE
def delete_user(request, id):
    if request.method == "DELETE":
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse({"message": "User deleted"})