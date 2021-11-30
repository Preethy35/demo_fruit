from django.shortcuts import render
from django.http import HttpResponse
from .models import Fruit1
# Create your views here.

# def home(request):
#     return HttpResponse("This is the Home page, WELCOME")
#
# def about(request):
#     return render(request,'about.html')
#
# def contact(request):
#     return HttpResponse("This is the contact page ")
#
# def detail(request):
#     return render(request,'detail.html')
#
# def thanx(request):
#     return render(request,'thanx.html')

# def operation(request):
#     return render(request,'operation.html')
#
# def result(request):
#     n1=int(request.GET['num1'])
#     n2=int(request.GET['num2'])
#     if 'add' in request.GET:
#         res=n1+n2
#     elif 'mul' in request.GET:
#         res=n1*n2
#     elif 'sub' in request.GET:
#         res=n2-n1
#     elif 'div' in request.GET:
#         if n2==0:
#             res="Zero by division"
#         else:
#             res=n1/n2
#     else:
#         res="Invalid Operation"
#
#     return render(request,'result.html',{'result':res})

def demo(request):
    fruit=Fruit1.objects.all()
    return render(request,'index.html',{'result':fruit})
