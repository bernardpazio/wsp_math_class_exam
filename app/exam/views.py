from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import Http404
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Exam, CompletedExam


def home(request):
    return redirect(exams)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(username=request.POST['email'],
                                                email=request.POST['email'],
                                                password=request.POST['password'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'])
            new_user.save()

            login(request, new_user)
            return redirect('exams')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def exams(request):
    return render(request, 'exams.html', {'exams': Exam.objects.all()})


@login_required
def completed_exams(request):
    return render(request, 'completed_exams.html', {
        'completed_exams': CompletedExam.objects.filter(user=request.user).order_by('-date')
    })


@login_required
def exam(request, exam_id):
    try:
        exam = Exam.objects.get(id=exam_id)
    except Exam.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        max_score = 0
        user_score = 0
        for question in exam.questions.all():
            for answer in question.answers.all():
                if answer.answer_value > 0:
                    max_score += answer.answer_value
                if f'{question.id}-{answer.id}' in request.POST:
                    user_score += answer.answer_value

        completed_exam = CompletedExam.objects.create(
            exam=exam,
            user=request.user,
            score=(user_score / max_score) * 100
        )
        completed_exam.save()
        return redirect(completed_exams)

    return render(request, 'exam.html', {'exam': exam})
