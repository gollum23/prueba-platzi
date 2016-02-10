from django.conf.urls import url

from .views import HomeView, SubscribeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^suscripcion/$', SubscribeView.as_view(), name='subscribe')
]