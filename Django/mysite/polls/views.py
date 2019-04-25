from django.shortcuts import render
from polls.models import Choice,jingdong


# Create your views here.
def blog_index(request):
    blog_list = Choice.objects.all()  # 获取所有数据
   # print(blog_list)
    return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面
def jingdong2(request):
   try:
      jingdong_list=jingdong.objects.all()
   except Exception as e:
      print(e)

   return render(request,'jingdong.html',{'jingdong_list':jingdong_list})