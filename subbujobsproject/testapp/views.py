from django.shortcuts import render
from testapp.models import Hydjobs
# Create your views here.
def home_view(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    jobs_list = Hydjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)

from testapp.models import Bngjobs
def bngjobs_view(request):
    jobs_list = Bngjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/bngjobs.html',my_dict)
from testapp.models import Punejobs
def punejobs_view(request):
    jobs_list = Bngjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',my_dict)
