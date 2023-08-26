from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    temlate = loader.get_template('bronze/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(temlate.render(context,request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render (request, 'bronze/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'bronze/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'bronze/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('bronze:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'bronze/index.html'
    context_object_name = 'latest_question_list'

    def get_ordering(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'bronze/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'bronze/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.

