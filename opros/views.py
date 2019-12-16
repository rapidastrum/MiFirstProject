from django.shortcuts import render
from django.http import HttpResponse


def start_quiz(request):
	return render(request, 'opros/opros.html')
