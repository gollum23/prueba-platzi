from django.conf.urls import url

from .views import HomeView, SubscribeView, SubscribeSuccessView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^suscripcion/$', SubscribeView.as_view(), name='subscribe'),
    url(r'^exito/$', SubscribeSuccessView.as_view(), name='success'),
]