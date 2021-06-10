from django.shortcuts import render
from tester.models import User


# Create your views here.
def index(request):
    return render(request,'tester/index.html')


def users(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'tester/users.html',context=user_dict)
