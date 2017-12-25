from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from index_app.models import SystemInfo
from index_app.serializers import SystemInfoSerializer
from rest_framework import generics
# from index_app.models import UserInfo
from django import forms

"""
# Create your views here.
# 应用：url, 名称,logo, 图片,类别
def get_system_message(data):
    #传入：
        1.sys_id
    #传出：
        1：url sys_url
        3：图片 sys_image
        4：name sys_name
        5:类别 sys_type

    #获取参数

    sys_id_list = date.json_args.sys_id()

    #检查参数
    # 查数据库
    for id in sys_id_list:
        sql= select * from   tablename  where sys_id= id ;
        db.excute(sql)
    

    return
"""

def index(request):
    return render(request, 'index.html')

class SystemInfoList(generics.ListCreateAPIView):
    queryset = SystemInfo.objects.all()
    serializer_class = SystemInfoSerializer


class SystemInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SystemInfo.objects.all()
    serializer_class = SystemInfoSerializer


class UserFrom(forms.Form):
    """
    Django admin后端form验证
    """
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


# 原来自己写的登录页，太丑现在用的admin登录页
def login(request):
    if request.method == 'POST':
        uf = UserFrom(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = UserInfo.objects.filter(username__exact=username, password__exact=password)

            if user:
                # return render_to_response('success.html', {"username": username})
                # return render(request, 'success.html', locals())
                return redirect('/admin/')
            else:
                # return HttpResponseRedirect('/login/')
                return redirect('/login/')
    else:
        uf = UserFrom()
    # return render_to_response('login.html', {'uf': uf})
    return render(request, 'login.html', locals())
