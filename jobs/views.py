from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.shortcuts import redirect, render
from .models import Job
from .forms import JobForm, ResumeForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            subject = f"New Job Posted: {form.instance.title}"
            message = f"{form.instance.company} has posted a job for {form.instance.title} at {form.instance.location}.\nApply here: {form.instance.apply_link}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['admin_email@example.com'])
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

def home(request):
    domain_filter = request.GET.get('domain')
    location_filter = request.GET.get('location')

    jobs = Job.objects.all()

    if domain_filter:
        jobs = jobs.filter(domain=domain_filter)
    if location_filter:
        jobs = jobs.filter(location__icontains=location_filter)
    return render(request, 'jobs/home.html', {'jobs': jobs})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'jobs/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'jobs/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
def apply_job(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = f"New Application for {form.instance.job.title}"
            message = f"{form.instance.name} applied for {form.instance.job.title}. Resume uploaded."
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['admin_email@example.com'])
            return redirect('home')
    else:
        form = ResumeForm()
    return render(request, 'jobs/apply.html', {'form': form})


