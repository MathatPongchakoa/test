from django.shortcuts import render
from .models import course_list
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
def courseList(request):
    c = course_list.objects.all()
    return render(request,'list_course.html',{'courses':c})

def course_idsearch(request):
    search = request.GET.get('course_id', None)  # รับค่าที่ส่งมาจากแบบฟอร์ม
    sa = course_list.objects.filter(course_id=search)  # ค้นหาข้อมูล
    return render(request, 'search.html', {'courses': sa})  # ส่ง context เป็น dict

class EditCourseView(UpdateView):
    model = course_list
    fields = ['course_name','t_name']
    template_name = 'edit.html'
    success_url = reverse_lazy('courseList')

class delete(DeleteView):
    model = course_list
    template_name = 'd.html'
    success_url = reverse_lazy('courseList')