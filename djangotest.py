def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, choice_text):
    question = get_object_or_404(Question, pk=choice_text)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, votes):
    votes += 1
    question = get_object_or_404(Question, pk=votes)
    return render(request, 'polls/votes.html', {'question': question})
    
    
detail.html:
    <h1>{{ question.question_text }}</h1>
    <ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }}</li>
    {% endfor %}
    </ul>

results.html:
    <h1>"You're looking at the results of question %s."</h1>
    <p>{{ choice.choice_text }}</p>

votes.html:
    <h1>"You're voting on question %s." % question_id</h1>
    <p>"Total votes: "{{ choice.votes }}</p>
