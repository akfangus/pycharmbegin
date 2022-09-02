from django.urls import path

from subscribeapp.views import SubsciptionView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubsciptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]
