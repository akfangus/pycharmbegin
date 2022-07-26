from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.form import AccountUpdateForm

from articleapp.models import Article

has_ownershop = [login_required, account_ownership_required]


# @login_required
# def hello_world(request):
#     # return HttpResponse('Hello world!!!!!!')
#     if request.method == 'POST':
#         # POST로 form 보냈을때 받아오는방법
#         temp = request.POST.get('hello_world_input')
#
#         # 받아온 데이터를 model에 저장하는방법
#         # 새로운 객체를 만들어서 거기에 넣고
#         # 마지막에 save까지 해줘야함.
#         # new_HelloWorld = HelloWorld()
#         # new_HelloWorld.text = temp
#         # new_HelloWorld.save()
#
#         # 모델 객체의 모든 정보를 가져옴
#         # hello_world_list = HelloWorld.objects.all()
#
#         # 받아온 데이터를 다시 html로 보낼때
#         # render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
#         return HttpResponseRedirect(reverse('accountapp:hello_world'))
#     else:
#         # 모델 객체의 모든 정보를 가져옴
#         # hello_world_list = HelloWorld.objects.all()
#         return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


# class base view가 훨씬 직관적이고 편하다. django의 좋은기능? 같음.
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # reverse 와 reverse_lazy의 차이? : reverse_lazy는 클래스에서만 사용할수 있다. 클래스안에서 reverse는 안됨. reverse는 함수형에서
    # submit성공했을때 redirect설정
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    # 이 두개만 있으면 됨
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownershop, 'get')
@method_decorator(has_ownershop, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/update.html'
    context_object_name = 'target_user'


@method_decorator(has_ownershop, 'get')
@method_decorator(has_ownershop, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'
    context_object_name = 'target_user'
