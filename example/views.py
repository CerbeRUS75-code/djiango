from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request, user, email):
    return HttpResponse(
        f"""
        <h2>О пользователе</h2>
        <p>Login: {user}</p>
        <p>Email: {email}</p>
    """
    )


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def user1(request, login, email):
    return HttpResponse(
        f"""
        <h2>Пользователь 1</h2>
        <p>Login: {login}</p>
        <p>Email: {email}</p>
    """
    )


def user2(request, login, email):
    return HttpResponse(
        f"""
        <h2>Пользователь 2</h2>
        <p>Login: {login}</p>
        <p>Email: {email}</p>
    """
    )
