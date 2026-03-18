from django.http import HttpResponse

def error_view(request):
    x = 10
    y = 2

    result = x / y

    return HttpResponse(result)