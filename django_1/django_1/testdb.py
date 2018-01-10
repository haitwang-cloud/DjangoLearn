from django.http import HttpResponse
from TestModel.models import Test

#数据库操作
def testdb(request):
    test1=Test(name='wht')
    test1.save()
    return HttpResponse("<p>add data Success</p>")