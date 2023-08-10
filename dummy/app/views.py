from django.shortcuts import render

from .models import Result

def list_view(request):
    results = Result.objects.all()
    context = {
        'results': results,
    }
    return render(request, 'app/result.html', context )
