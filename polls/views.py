from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
	template_name = "polls/index.html"
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('pub_date')[:5]

class DetailView(generic.DetailView):
	template_name = "polls/detail.html"
	model = Question

# ---------------------------------------------------------------
def hello(request):
	return HttpResponse("Hello world")
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