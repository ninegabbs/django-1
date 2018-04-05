from django.shortcuts import render

from django.http import HttpResponse

from .models import Question, Choice

def hello(request):
	return HttpResponse("Hello world")

def index(request):
	return HttpResponse("Index Page")

# Returns all questions and their choices as a list in one line
def questions(request):
	result = []
	for q in Question.objects.all():
		result.append(q)
		result.append("\n")
		for c in q.choice_set.all():
			result.append(c)
			result.append("\n")
	return HttpResponse(result)