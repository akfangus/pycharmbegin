from django.urls import path

from subscribeapp.views import SubsciptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubsciptionView.as_view(), name='subscribe')
]
