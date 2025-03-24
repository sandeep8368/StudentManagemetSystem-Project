from django.shortcuts import render
from app.models import studentModel
# Create your views here.
def display_view(request):
    student_data = studentModel.objects.all()
    context = {'student': student_data}
   
    return render(request,'html/index.html',context)