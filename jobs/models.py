from django.db import models

class Job(models.Model):
    DOMAIN_CHOICES = [
        ('IT', 'IT'),
        ('Non-IT', 'Non-IT'),
        ('Internship', 'Internship'),
        ('Government', 'Government'),
    ]
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    apply_link = models.URLField()
    posted_on = models.DateField(auto_now_add=True)
    domain = models.CharField(max_length=20, choices=DOMAIN_CHOICES, default='IT')

    def __str__(self):
        return self.title

class Resume(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume_file = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"

