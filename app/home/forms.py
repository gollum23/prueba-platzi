from django import forms
# from django.contrib.auth.forms import UserCreationForm

# Create tupla with months 01-12
MONTHS = (
    ('{}'.format(i) if i > 9 else '0{}'.format(i), '{}'.format(i) if i > 9 else '0{}'.format(i)) for i in range(1, 13)
)

# Create tupla with years 2016-2049
YEARS = ((i, i) for i in range(2016, 2050))


class SubscriptionForm(forms.Form):
    username = forms.CharField(
        label='Usuario',
        max_length=30
    )
    password1 = forms.CharField(
        required = True,
        widget = forms.PasswordInput(render_value = False),
        label = 'Password',
        min_length=8,
        max_length=50
    )
    password2 = forms.CharField(
        required = True,
        widget = forms.PasswordInput(render_value = False),
        label = 'Password confirmation',
        min_length=8,
        max_length=50
    )
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
        max_value=9999999999999999,
        widget=forms.TextInput(
            attrs={'data-stripe': 'number'}
        )
    )
    card_name = forms.CharField(
        max_length=50,
        label='Nombre como aparece en la tarjeta'
    )
    card_month = forms.ChoiceField(
        label='Mes de vencimiento',
        choices=MONTHS,
        widget=forms.Select(
            attrs={'data-stripe': 'exp-month'}
        )
    )
    card_year = forms.ChoiceField(
        label='Año de vencimiento',
        choices=YEARS,
        widget=forms.Select(
            attrs={'data-stripe': 'exp-year'}
        )
    )
    card_cvc = forms.IntegerField(
        max_value=999,
        min_value=0,
        label='Código de seguridad',
        widget=forms.TextInput(
            attrs={'data-stripe': 'cvc'}
        )
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no son iguales')
        return cleaned_data

