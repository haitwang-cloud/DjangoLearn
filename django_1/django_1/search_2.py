from django.shortcuts import render
from django.views.decorators import csrf
"""
 在模板的末尾，我们增加一个 rlt 记号，为表格处理结果预留位置。
表格后面还有一个{% csrf_token %}的标签。csrf 全称是 Cross Site Request Forgery。
这是Django提供的防止伪装提交请求的功能。POST 方法提交的表格，必须有此标签。 
"""
#接受post请求数据
def search_post(request):
    ctx={}
    if request.POST:
        ctx['rlt']=request.POST['q']
    return render(request,"post.html",ctx)