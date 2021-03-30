from django.shortcuts import render, redirect
from datetime import date
from django.contrib import messages

from .models import Course

# Create your views here.
def add_course(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'add_course.html', context)

def create(request):
    errors = Course.objects.validate_course(request.POST)
    if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    else:
        Course.objects.create(
        name=request.POST['course_name'],
        desc=request.POST['description'],
        add_date= date.today()
    )
    return redirect('/')

def delete_confirm(request, id):
    context ={
        'course': Course.objects.get(id=id)
    }
    return render(request, 'delete_confirm.html', context)

def delete(request, id):
    show_to_delete = Course.objects.get(id=id)
    show_to_delete.delete()
    return redirect('/')