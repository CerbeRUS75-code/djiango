from django import forms


class UserForm(forms.Form):
    user = forms.CharField(
        label="Пользователь",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )


class OrderForm(forms.Form):
    ru_months = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь",
    }

    product = forms.ChoiceField(
        label="Товар",
        choices=[("1", "Товар 1"), ("2", "Товар 2")],
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    quantity = forms.IntegerField(
        label="Количество",
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    customer_name = forms.CharField(
        label="Имя клиента",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    delivery_date = forms.DateField(
        label="Дата доставки",
        widget=forms.SelectDateWidget(
            months=ru_months,
            attrs={"class": "form-select form-select-sm d-inline w-auto"},
        ),
    )
    comment = forms.CharField(
        label="Комментарий",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        required=False,
    )
    agree_terms = forms.BooleanField(
        label="Согласен с условиями",
        required=True,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
