from django.shortcuts import render
# from django.shortcuts import render
from .models import Case

# Create your views here.



def home(request):
    cases = Case.objects.all()
    return render(request, 'index.html', {'cases': cases})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def donate(request):
    try:
        case = Case.objects.get(pk=1)  # Replace with an actual primary key that exists
    except Case.DoesNotExist:
        case = None
    return render(request, 'donate.html', {'case': case})


def faq(request):
    return render(request, 'faqs.html')

def cases(request):
    cases = Case.objects.all()
    return render(request, 'cases.html', {'cases': cases})

def single_cases(request):
    cases = Case.objects.all()
    return render(request, 'single-cases.html', {'cases': cases})

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request):
    return render(request, 'blog-details.html')

def gallery(request):
    return render(request, 'gallery.html')

def volunteer(request):
    return render(request, 'volunteer.html')

def error(request):
    return render(request, 'error.html')



