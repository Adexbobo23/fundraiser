from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Case , Donation
from .forms import DonationForm
from django.db import transaction
from decimal import Decimal
from django.http import JsonResponse

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

# def single_cases(request):

#     cases = Case.objects.all()
#     return render(request, 'single-cases.html', {'cases': cases})


def case_detail(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    amounts = [2500, 10000]
    
    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                form = DonationForm(request.POST)
                if form.is_valid():
                    with transaction.atomic():
                        # Create the donation record
                        donation = Donation.objects.create(
                            case=case,
                            amount=form.cleaned_data['final_amount'],
                            donation_type=form.cleaned_data['donation_type'],
                            first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            email=form.cleaned_data['email'],
                            comment=form.cleaned_data['comment'],
                            anonymous=form.cleaned_data['anonymous_donation'],
                        )
                        
                        if form.cleaned_data['donation_type'] == 'regular':
                            case.raised_amount += form.cleaned_data['final_amount']
                            case.progress = (case.raised_amount / case.goal_amount) * 100
                            case.save()
                        
                        # Here you would integrate with your payment processor
                        # payment_result = process_payment(donation)
                        # if payment_result.requires_redirect:
                        #     return JsonResponse({
                        #         'redirect_url': payment_result.redirect_url
                        #     })
                        
                        return JsonResponse({
                            'success': True,
                            'message': 'Thank you for your donation!'
                        })
                else:
                    return JsonResponse({
                        'success': False,
                        'message': 'Please correct the errors below.',
                        'errors': form.errors
                    }, status=400)
                    
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': 'An error occurred while processing your donation.'
                }, status=500)
        else:
            
            pass
    
    context = {
        'case': case,
        'form': DonationForm(),
        'amounts': amounts,
        'min_amount': Decimal('100'),
    }
    
    return render(request, 'single-cases.html', context)


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
 
def beneficiary_dashboard(request):
    cases = Case.objects.filter(beneficiary=request.user)

    # Collect data for chart
    chart_data = {
        "labels": [case.title for case in cases],
        "progress": [case.progress_percentage for case in cases],
    }

    return render(request, 'beneficiary-dashboard.html',{"chart_data": chart_data}) 









