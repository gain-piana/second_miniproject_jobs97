from django.shortcuts import render, get_object_or_404
# from django.views.generic.base import TemplateView
from .models import JobsTest
from .models import ReviewTests
# class MainpageView(TemplateView):
#     template_name = 'jobs97test/index.html'

def jobs97_all(request):
    # print("hello")
    datas = ReviewTests.objects.all()
    defalut_info = get_object_or_404(ReviewTests, pk=1)
    # defalut_info = "헬로"
    print(defalut_info)
    
    return render(request, 'jobs97test/index.html',{'datas':datas, 'defalut_info':defalut_info})


def jobs97_click(request, pk):

    # 선택한 항목을 form객체에 넣어서 응답하기
    # pk에 대한 데이터 레코드를 읽어오기
    print(pk)
    datas = ReviewTests.objects.all()
    datas2 = get_object_or_404(ReviewTests, pk=pk)
    
    return render(request, 'jobs97test/index2.html', {'datas':datas,'datas2':datas2})
