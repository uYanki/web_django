from django.shortcuts import render,redirect
from django import forms

# Create your views here.
from mgr.models import UserInfo
def user_list(request):
    return render(request,'user_list.html',{'userinfos':UserInfo.objects.all()})

# 自动生成表单
# class UserModelForm(forms.ModelForm):

def user_add(request):
    if request.method=='GET':
        return render(request, 'user_add.html')
    UserInfo.objects.create(username=request.POST.get("username"),
                            password=request.POST.get("password"),
                            age=request.POST.get("age"),
                            phone=request.POST.get("phone"))
    return redirect('/')

def user_del(request,uid):
    try:
        UserInfo.objects.get(id=uid).delete()
        # return render(request,"user_info.html",{'info':"ok"})
        return redirect('/')
    except:
        return render(request, "user_info.html", {'info': "error: User doesn't exist!"})

def user_edit(request,uid):
    try:
        if request.method == 'GET':
            return render(request,"user_edit.html",{'userinfo':UserInfo.objects.get(id=uid)})
        UserInfo.objects.get(id=request.POST.get("id")).update(username=request.POST.get("username"),
                                            password=request.POST.get("password"),
                                            age=request.POST.get("age"),
                                            phone=request.POST.get("phone"))
        return redirect('/')
    except:
        return render(request,"user_info.html",{'info':"error: User doesn't exist!"})

def user_update(request):
    try:
        # 写法1
        UserInfo.objects.filter(id=request.POST.get("id")).update(username=request.POST.get("username"),
                                                                  password=request.POST.get("password"),
                                                                  age=request.POST.get("age"),
                                                                  phone=request.POST.get("phone"))
        # 写法2
        # uid = request.POST['id']
        # obj = UserInfo.objects.get(id=uid) # 获取对象
        # obj.username = request.POST['username']
        # obj.password = request.POST['password']
        # obj.age = request.POST['age']
        # obj.phone = request.POST['phone']
        # obj.save() # 保存修改
        return redirect('/')
    except:
        return render(request,"user_info.html",{'info':"error: User doesn't exist!"})
