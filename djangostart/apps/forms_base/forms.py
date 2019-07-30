from django import forms
from . import models

class ContactForm(forms.Form):
    subject = forms.CharField(
        label="主题",
        min_length=8,
        required=True,
        # initial="Django_Form",
        error_messages={
            "min_length": "主题至少是8个字符",
            "required": "主题是必填项",
        },
    )
    content = forms.CharField(
        label="正文",
        widget=forms.Textarea,
    )
    content2 = forms.CharField(
        label="正文2",
        widget=forms.Textarea(
            attrs={
                "class":"clasa",
                "style":"color:red;font-size:20px",
            }
        )
    )
    sender = forms.EmailField(label="发送人")
    cc_myself = forms.BooleanField(label="抄送")
    # 密码字段
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    # 单radio值为字符串
    gender = forms.fields.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect()
    )
    # 下拉选择
    hobby = forms.fields.ChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
    #  多选
    hobby2 = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )
    # 单选checkbox
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )
    # 多选checkbox
    hobby3 = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="输入密码",max_length=128,widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码",max_length=128,widget=forms.PasswordInput)
    class Meta:
        model = models.UserInfo
        fields = ('username','password')

    def clean_username(self):
        users = models.UserInfo.objects.filter(username=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        else:
            raise forms.ValidationError("该用户名已经被使用")

    def clean(self):
        if self.cleaned_data["password"]!=self.cleaned_data["password"]:
            raise forms.ValidationError("密码不一致")

class LoginForm(forms.ModelForm):
    """登录表单"""
    password = forms.CharField(label="密码", max_length=30, widget=forms.PasswordInput(attrs={"size": 20, }))

    def clean_username(self):
        user = models.UserInfo.objects.filter(username__iexact=self.cleaned_data["username"])
        if not user:
            raise forms.ValidationError("用户不存在")
        else:
            return self.cleaned_data["username"]

    class Meta:
        model = models.UserInfo
        exclude = ()
