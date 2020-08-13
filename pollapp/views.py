from django.shortcuts import render,redirect
from .models import Question,Choice
# Create your views here.

def home(request):
    question = Question.objects.all()

    content = {
        "question":question

    }
    return  render(request, "pollapp/home.html",content)


def votes(request,pk):
    question = Question.objects.get(id=pk)

    try:
        choice = question.choice_set.get(id=request.POST["choices"])

    except KeyError:
        print("Failed To Vote")

    else:
        choice.votes += 1
        choice.save()
        return redirect("results", pk=question.id)
    content = {
        "question":question

    }
    return render(request, "pollapp/votes.html",content)


def results(request,pk):
    question = Question.objects.get(id=pk)

    content = {
        "question":question
    }

    return render(request, "pollapp/results.html",content)