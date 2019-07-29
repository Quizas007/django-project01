from django.shortcuts import render,HttpResponse
from .models import UserInfo
# Create your views here.


def demo01(request):
    # return HttpResponse("helloworld")
    return render(request, "app01/demo01.html")

def demo_form(request):
    email = request.GET.get("email")
    info = request.GET
    passwd = info["password"]
    return render(request, "app01/demo_form.html", {"user":email, "mima":passwd})


def demo_form_post(request):
    userlist = {"chen@123":"12345"}
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email in userlist.keys() and password==userlist[email]:
            return HttpResponse("Welcome!")
        return render(request, "app01/demo_form_post.html")
    return render(request, "app01/demo_form_post.html")

def demo_form_db(request):
    # userlist = UserInfo.objects.all()
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            ret = UserInfo.objects.get(email=email)
            if ret and ret.password==password:
                return HttpResponse("Welcome!")
            else:
                msg = "用户名密码错误"
        except Exception as ex:
            msg = "用户不存在"
        kwgs = {
            "msg":msg

        }
        return render(request, "app01/demo_form_db.html", kwgs)
    return render(request, "app01/demo_form_db.html")

