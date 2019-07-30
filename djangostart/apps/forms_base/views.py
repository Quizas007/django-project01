from django.shortcuts import render
from .forms import ContactForm,RegisterForm
from .models import UserInfo
# Create your views here.

def index(request):
    form = ContactForm(request.GET)
    return render(request,'forms_base/index.html',{"form":form})

def register(request):
    reg_form = RegisterForm()
    if request.method == "POST":
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data["username"]
            password = reg_form.cleaned_data["password"]
            print("合法")
        else:
            print("不合法")
    return render(request,'forms_base/register.html',{"form":reg_form})

def login(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        # is_valid提交的数据合法(会检查所有字段及表单整体的合法性)
        if login_form.is_valid():
            password = login_form.cleaned_data["password"]
            user = UserInfo.objects.get(username=login_form.cleaned_data["username"])
    return render(request, 'forms_base/login.html', {"form": login_form})


def logout(request):
    print('退出成功')
    return HttpResponse("退出成功")