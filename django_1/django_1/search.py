#接受用户的请求
from django.http import HttpResponse
from django.shortcuts import render_to_response

#表单
def search_form(request):
    return render_to_response("search_form.html")
#接受请求数据

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message='Content:'+request.GET['q']
    else:
        message='Empty Form'
    return HttpResponse(message)
