from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    q_list = Question.objects.order_by('-create_date')
    return render(request, 'pybo/question_list.html', {'question_list' : q_list})

def detail(request,question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request,'pybo/question_detail.html', {
        'question' : q
    })

@login_required(login_url='common:login')
def answer_create(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()


    context = {'form' : form }
    return render(request, 'pybo/question_form.html', context)
