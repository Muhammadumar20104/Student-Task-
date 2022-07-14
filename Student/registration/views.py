from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def register(request):
    # S = Student.objects.all()
    S = Student.objects.get(id = 2)

    print(S)
    return render(request,'register.html',context={"stu":S})

# Create your views here.
