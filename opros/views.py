from django.shortcuts import render
from django.http import HttpResponse
from opros.models import TextAnswer, Question

counter = 0


def start_test(request):
    global counter
    counter = 0
    return render(request, 'opros/startOpros.html')


def get_question(request):
    global counter
    counter += 1
    try:
        q = Question.objects.get(id=counter)
    except:
        return render(request, 'opros/endOpros.html')
    return render(request, 'opros/opros.html', {'question': q})
