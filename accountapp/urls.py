from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    # path('hello_world/', hello_world, name='hello_world'),
    # 클래스형 view를 넣을때는 .as_view()를 추가해야한다고함.
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    # login view
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
