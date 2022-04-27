from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    # raise Http404('error')
    # print(reverse("index"))
    # print(reverse('articles', args=(1, 2)))  # 在反向解析中填入参数
    # print(reverse('articles', kwargs={"year":2, "month":3}))  # 在反向解析中填入参数
    # return HttpResponse("index")
    # return HttpResponseRedirect(reverse('articles', args=(1, 2)))
    return redirect(reverse('articles', args=(1, 2)))

def articles(request,year,month):
    return HttpResponse("%d.%d"%(year,month))

def blogs(request,year,month):
    return HttpResponse("%s.%s"%(year,month))

def pages(request):
    return render(request,"mysite.html")

def func(request): # 反向解析
    print(reverse("index")) # 输出 /myapp/
    # 在反向解析中填入参数
    print(reverse('articles', args=(1, 2))) # 输出 /myapp/articles/1/2/
    print(reverse('articles', kwargs={"year":1, "month":2})) # 输出 /myapp/articles/1/2/
    # return HttpResponseRedirect(reverse('articles', args=(1, 2)))
    return redirect(reverse('articles', args=(11, 2)))