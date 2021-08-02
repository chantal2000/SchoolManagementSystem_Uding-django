from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .forms import StudentRegistrationForm
from django.shortcuts import render

# Create your views here.
def register_student(request):
    form=StudentRegistrationForm()
    return render(request,"register_student.htm",{"form":form})

# @login_required
# def index(request):
#     return render(request,"home.htm")
# def student_list(request):
#     students=Student.objects.all()
#     paginator=Paginator(students,1)
#     paged_students=paginator.get_page(page)


# def single_student(request,student_id):
#     single_student=get_object_or_404(StudentInfo,pk=student_id)
