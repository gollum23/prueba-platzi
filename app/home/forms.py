from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create tupla with months 01-12
MONTHS = (
    ('{}'.format(i) if i > 9 else '0{}'.format(i), '{}'.format(i) if i > 9 else '0{}'.format(i)) for i in range(1, 13)
)

# Create tupla with years 2016-2049
YEARS = ((i, i) for i in range(2016, 2050))


class SubscriptionForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nombres',
        max_length=30,
    )
    last_name = forms.CharField(
        label='Apellidos',
        max_length=30,
    )
    email = forms.EmailField(
        label='Correo electrónico'
    )
    card_number = forms.IntegerField(
        label='Número de tarjeta',
        max_value=9999999999999999
    )
    card_name = forms.CharField(
        max_length=50,
        label='Nombre como aparece en la tarjeta'
    )
    card_month = forms.ChoiceField(
        label='Mes',
        choices=MONTHS
    )
    card_year = forms.ChoiceField(
        label='Año',
        choices=YEARS
    )
    card_cvc = forms.IntegerField(
        max_value=999,
        min_value=0
    )

