from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Course, Lesson, Faq, FaqData, Quiz, QuizData


# Create your views here.


def index(request):
    return render(request=request, template_name="index.html")


def welcome(request):
    return render(request=request, template_name="welcome.html")


def lessons(request):
    course_id = request.GET.get("id")
    course = {}
    course_lessons = []
    if course_id is not None:
        course = Course.objects.filter(id=course_id).all()[0]
        course_lessons = Lesson.objects.filter(course_id=course_id).all()
        for lesson in course_lessons:
            lesson.domId = "dom" + str(lesson.id)
    queryset = Course.objects.all()
    context = {"courses": queryset, "lessons": course_lessons, "course": course}
    return render(request, "lessons.html", context=context)


def faq(request):
    queryset = Faq.objects.all()[0]
    faqs_data = FaqData.objects.filter(faq_id=queryset.id).all()
    for field in faqs_data:
        field.domId = "dom" + str(field.id)
    context = {"faq": queryset, "faqs_data": faqs_data}
    return render(request, "faq.html", context=context)


def quiz(request):
    quiz_id = request.GET.get("id")
    selected_quiz = {}
    quiz_questions = []
    if quiz_id is not None:
        selected_quiz = Quiz.objects.filter(id=quiz_id).all()[0]
        quiz_questions = QuizData.objects.filter(quiz_id=quiz_id).all()
        for field in quiz_questions:
            field.domId = "dom" + str(field.id)
    queryset = Quiz.objects.all()
    context = {"quizzes": queryset, "questions": quiz_questions, "quiz": selected_quiz}
    return render(request, "quiz.html", context=context)


def certificate(request):
    return render(request=request, template_name="certificate.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("welcome")
        messages.error(request, "Registration failed. Please check the requirements below.")
        return redirect("register_request")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You have successfully logged in.")
                return redirect("welcome")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")
