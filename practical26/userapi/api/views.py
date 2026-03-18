from django.http import JsonResponse

def user_list(request):

    users = [
        {"id": 1, "name": "John", "email": "john@example.com"},
        {"id": 2, "name": "Alice", "email": "alice@example.com"},
        {"id": 3, "name": "Bob", "email": "bob@example.com"}
    ]

    return JsonResponse(users, safe=False)