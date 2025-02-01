from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import JobDescription, ScreeningTask

@login_required
def screening_view(request):
    return render(request, 'screening/screening.html') 