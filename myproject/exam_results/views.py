# exam_results/views.py
from django.shortcuts import render
from .models import ExamResult

def home(request):
    exam_results = ExamResult.objects.all()
    return render(request, 'home.html', {'exam_results': exam_results})
