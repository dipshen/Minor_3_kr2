from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import PersonalInfo, EducationalProgram, Management, Classmate, PageContent, Student
from django.db.models import Q

def home_view(request):
    personal_info = PersonalInfo.objects.first()
    page_content = PageContent.objects.filter(page_name='personal').first()
    return render(request, 'myapp/home.html', {
        'personal_info': personal_info,
        'page_content': page_content,
    })

def program_view(request):
    # Create or update the program information
    program, created = EducationalProgram.objects.get_or_create(
        name="Дизайн",
        defaults={
            'program_url': "https://design.hse.ru/",
            'subjects': "Дизайн и программирование",
            'skills': "Делать сайты и приложения",
            'advantages': "Изучение и дизайна, и кода",
            'prospects': "Стану уникальным специалистом и смогу устроиться в классные компании"
        }
    )
    if not created:
        program.program_url = "https://design.hse.ru/"
        program.subjects = "Дизайн и программирование"
        program.skills = "Делать сайты и приложения"
        program.advantages = "Изучение и дизайна, и кода"
        program.prospects = "Стану уникальным специалистом и смогу устроиться в классные компании"
        program.save()
    
    page_content = PageContent.objects.filter(page_name='program').first()
    return render(request, 'myapp/program.html', {
        'program': program,
        'page_content': page_content,
    })

def students_view(request):
    # Обработка формы добавления студента
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        educational_program = request.POST.get('educational_program')
        course = request.POST.get('course')
        
        if full_name and educational_program and course:
            Student.objects.create(
                full_name=full_name,
                educational_program=educational_program,
                course=int(course)
            )
            return redirect('myapp:students')

    # Получение параметров фильтрации и сортировки
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'full_name')
    course_filter = request.GET.get('course', '')

    # Фильтрация студентов
    students = Student.objects.all()
    if search_query:
        students = students.filter(
            Q(full_name__icontains=search_query) |
            Q(educational_program__icontains=search_query)
        )
    if course_filter:
        students = students.filter(course=int(course_filter))

    # Сортировка
    students = students.order_by(sort_by)

    context = {
        'students': students,
        'search_query': search_query,
        'sort_by': sort_by,
        'course_filter': course_filter,
        'courses': range(1, 5),  # для выпадающего списка курсов
    }
    return render(request, 'myapp/students.html', context)

class ManagementView(ListView):
    model = Management
    template_name = 'myapp/management.html'
    context_object_name = 'management_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_content'] = PageContent.objects.filter(page_name='management').first()
        context['academic_leaders'] = Management.objects.filter(role='academic_lead')
        context['managers'] = Management.objects.filter(role='manager')
        return context

class ClassmatesView(ListView):
    model = Classmate
    template_name = 'myapp/classmates.html'
    context_object_name = 'classmates'

    def get_queryset(self):
        queryset = Classmate.objects.all()
        
        # Filtering
        name_filter = self.request.GET.get('name', '')
        if name_filter:
            queryset = queryset.filter(full_name__icontains=name_filter)

        # Sorting
        sort_by = self.request.GET.get('sort', 'full_name')
        if sort_by in ['full_name', 'email']:
            queryset = queryset.order_by(sort_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_content'] = PageContent.objects.filter(page_name='classmates').first()
        
        # Add statistics
        context['total_classmates'] = self.get_queryset().count()
        return context

def about(request):
    return render(request, 'about.html')

def animals(request):
    return render(request, 'animals.html')

def check_words(request):
    correct_words = []  

    if request.method == 'POST':
        words = request.POST.get('words', '').split(', ')
        lengths = request.POST.get('lengths', '').split()
        lengths = [int(length) for length in lengths]  
        correct_words = [words[i] for i in range(len(words)) if len(words[i]) == lengths[i]]

    context = {
        'correct_words': correct_words,
        'words': request.POST.get('words', ''),  
        'lengths': request.POST.get('lengths', '')  
    }
    return render(request, 'check_words.html', context)

def requirements(request):
    return render(request, 'requirements.html')


def rectangle_fit(request):
    result = None  

    if request.method == 'POST':
        a = float(request.POST.get('a', 0))
        b = float(request.POST.get('b', 0))
        c = float(request.POST.get('c', 0))
        d = float(request.POST.get('d', 0))

        
        if (a <= c and b <= d) or (a <= d and b <= c):
            result = "Прямоугольник со сторонами a и b МОЖЕТ уместиться внутри прямоугольника со сторонами c и d."
        else:
            result = "Прямоугольник со сторонами a и b НЕ МОЖЕТ уместиться внутри прямоугольника со сторонами c и d."

    context = {
        'result': result,
        'a': request.POST.get('a', ''), 
        'b': request.POST.get('b', ''),
        'c': request.POST.get('c', ''),
        'd': request.POST.get('d', '')
    }
    return render(request, 'rectangle_fit.html', context)