from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)


def index(request):
    return HttpResponse("Index")


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about/")


def details(request):
    return HttpResponsePermanentRedirect("/")


def people_index(request, id):
    people = ["Alex", "Bob", "Sam"]
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    return HttpResponseNotFound("Not Found")


def access(request, age):
    if age not in range(1, 90):
        return HttpResponseBadRequest("Некорректные данные")
    if age > 17:
        return HttpResponse("Доступ разрешен")
    return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
