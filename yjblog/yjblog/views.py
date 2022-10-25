# _*_ coding:utf-8 _*_


from django.shortcuts import render
from django.views import View


# 主页
class Home(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        pass


# 404页面
def page_not_found(request, exception=None):
    return render(request, '404.html')


