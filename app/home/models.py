from django.contrib.auth.models import User
from django.db import models


class SubscriptionUserData(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Usuario'
    )
    amount = models.SmallIntegerField(
        verbose_name='Monto o cantidad'
    )
    payment_date = models.DateTimeField(
        verbose_name='Fecha de pago'
    )
    stripe_id = models.CharField(
        verbose_name='ID Cliente recurente de Stripe',
        max_length=255
    )

    class Meta:
        verbose_name = 'Datos de suscripción'
        verbose_name_plural = 'Datos de suscripción'

    def __str__(self):
        return '{} pago el {}'.format(self.user.get_full_name(), self.payment_date)
