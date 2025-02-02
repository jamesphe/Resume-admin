from django.shortcuts import render, get_object_or_404
from .models import Candidate

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/candidate_list.html', {'candidates': candidates})

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'candidates/candidate_detail.html', {'candidate': candidate}) 