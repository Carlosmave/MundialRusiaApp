from django.shortcuts import render
from django.http import HttpResponse
from .models import trivia
# Create your views here.
def index(request):
    #return HttpResponse('Hello from Trivia')
    Trivia=trivia.objects.all()[:10]
    context = {
        'question':'Next Question',
        'trivia': Trivia
    }
    return render(request, 'trivia/index.html', context)

def details(request, id):
    triv = trivia.objects.get(id=id)
    context={
    'triv':triv
    }
    return render(request, 'trivia/details.html', context)
