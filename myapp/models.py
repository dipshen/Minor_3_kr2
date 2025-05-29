from django.db import models

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.TextField()

    def __str__(self):
        return self.full_name

class EducationalProgram(models.Model):
    name = models.CharField(max_length=200)
    program_url = models.URLField()
    subjects = models.TextField()
    skills = models.TextField()
    advantages = models.TextField()
    prospects = models.TextField()

    def __str__(self):
        return self.name

class Management(models.Model):
    ROLE_CHOICES = [
        ('academic_lead', 'Academic Leader'),
        ('manager', 'Manager'),
    ]
    
    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    photo = models.ImageField(upload_to='management_photos/')
    email = models.EmailField()

    def __str__(self):
        return f"{self.get_role_display()}: {self.full_name}"

class Classmate(models.Model):
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='classmate_photos/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class PageContent(models.Model):
    PAGE_CHOICES = [
        ('personal', 'Personal Page'),
        ('program', 'Educational Program'),
        ('management', 'Management'),
        ('classmates', 'Classmates'),
    ]
    
    page_name = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_page_name_display()

class Student(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Имя и Фамилия')
    educational_program = models.CharField(max_length=100, verbose_name='Образовательная программа')
    course = models.IntegerField(verbose_name='Курс')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['full_name', 'course']
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.full_name} - {self.educational_program} ({self.course} курс)"