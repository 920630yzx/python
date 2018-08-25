from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("sunck is a good man")

from .models import Grades
def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板在渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myApp/grades.html', {"grades":gradesList})