from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "Главная страница",
        content_type="text/html; charset=utf-8",
        status=200,
        headers={"SecretCode": "5555577777"},
    )


def request_info(request):
    return HttpResponse(
        f"""
        <h2>HttpRequest</h2>
        <p><b>scheme:</b> {request.scheme}</p>
        <p><b>path:</b> {request.path}</p>
        <p><b>method:</b> {request.method}</p>
        <p><b>GET:</b> {request.GET}</p>
        <p><b>headers:</b> {dict(request.headers)}</p>
        <p><b>get_full_path:</b> {request.get_full_path()}</p>
        <p><b>get_host:</b> {request.get_host()}</p>
        <p><b>get_port:</b> {request.get_port()}</p>
    """,
        content_type="text/html; charset=utf-8",
    )


def user(request, name="Alex", code=345):
    return HttpResponse(f"<h2>Имя: {name} код {code}</h2>")


def products(request, id):
    return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")
