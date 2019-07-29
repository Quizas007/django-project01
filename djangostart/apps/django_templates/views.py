from django.shortcuts import render

# Create your views here.


def index(request):
    kwgs = {
        "plmm" : [
            {"name":"研","desc":"plmm1","img":"/static/django_templates/django_html_files/1.JPG"},
            {"name":"雅","desc":"plmm2","img":"/static/django_templates/django_html_files/2.JPG"},
            {"name":"馨","desc":"plmm3","img":"/static/django_templates/django_html_files/3.PNG"},
            {"name":"chen","desc":"plmm4","img":"/static/django_templates/django_html_files/4.JPG"},
        ]
    }
    return render(request, 'django_templates/index.html',kwgs)