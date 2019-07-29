from django.shortcuts import render,redirect,reverse
from .models import UserInfo

# Create your views here.


def index(request):
    users = UserInfo.objects.all().values()
    users = list(users)
    user_list = {}
    user_email = []
    user_password = []
    for user in users:
        user_email.append(user["email"])
        user_password.append(user["password"])
    user_list["email"] = user_email
    user_list["password"] = user_password
    print(user_list)
    return render(request, "u_system/index.html", user_list)


def login(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            ret = UserInfo.objects.get(email=email)
            if ret and ret.password==password:
                # return redirect("/index/")
                return redirect(reverse('u_system:index'))
            else:
                msg = "用户名密码错误"
        except Exception as ex:
            msg = "用户不存在"
        kwgs = {
            "msg":msg
        }
        return render(request, "u_system/login.html", kwgs)
    return render(request, "u_system/login.html")

def reg(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        UserInfo.objects.create(email=email,password=password)
        return render(request, "u_system/login.html")
    return render(request, "u_system/reg.html")