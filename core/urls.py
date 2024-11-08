from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('faq/', views.faq, name='faq'),
    path('cases/', views.cases, name='cases'),
    path('single_cases/', views.single_cases, name='single_cases'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('error/', views.error, name='error'),
    
]


# urlpatterns = [
#     path('', home, name='home'),
# ]