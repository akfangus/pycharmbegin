from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello world!!!!!!')
    if request.method == 'POST':
        # POST로 form 보냈을때 받아오는방법
        temp = request.POST.get('hello_world_input')

        # 받아온 데이터를 model에 저장하는방법
        # 새로운 객체를 만들어서 거기에 넣고
        # 마지막에 save까지 해줘야함.
        new_HelloWorld = HelloWorld()
        new_HelloWorld.text = temp
        new_HelloWorld.save()

        # 받아온 데이터를 다시 html로 보낼때
        return render(request, 'accountapp/hello_world.html', context={'HelloWorld_output': new_HelloWorld})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!'})
