from django.shortcuts import render

from .forms import OrderForm, UserForm


def forms_page(request):
    result = None

    django_form = UserForm(prefix="django")
    order_form = OrderForm(prefix="order")

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "manual":
            user = request.POST.get("manual_user", "")
            email = request.POST.get("manual_email", "")
            result = f"HTML-форма: пользователь {user}, email: {email}"

        elif form_type == "django":
            django_form = UserForm(request.POST, prefix="django")
            if django_form.is_valid():
                data = django_form.cleaned_data
                result = f"Django Form: пользователь {data['user']}, email: {data['email']}"

        elif form_type == "order":
            order_form = OrderForm(request.POST, prefix="order")
            if order_form.is_valid():
                data = order_form.cleaned_data
                product_map = {"1": "Товар 1", "2": "Товар 2"}
                product_name = product_map.get(data["product"], data["product"])
                result = (
                    "Сложная форма: "
                    f"товар {product_name}, количество {data['quantity']}, "
                    f"клиент {data['customer_name']}, email {data['email']}"
                )

    return render(
        request,
        "forms_page.html",
        context={
            "title": "Django Forms",
            "header": "Формы Django",
            "django_form": django_form,
            "order_form": order_form,
            "result": result,
        },
    )
