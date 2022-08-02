from django.contrib import admin
from django.urls import path, include

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # 클래스형 view를 넣을때는 .as_view()를 추가해야한다고함.
    path('create/', AccountCreateView.as_view(), name='create')
]
