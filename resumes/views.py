from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Resume, ResumeAnalysis

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(uploaded_by=request.user)
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})

@login_required
def resume_detail(request, pk):
    resume = Resume.objects.get(pk=pk)
    return render(request, 'resumes/resume_detail.html', {'resume': resume}) 