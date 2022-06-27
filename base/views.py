from django.shortcuts import render,redirect

from base.forms import LeadForm
from .models import Discount, Lesson, Lead

# Create your views here.

def home(request):

    discount = Discount.objects.get(id=1)
    lessons = Lesson.objects.all()

    
    if request.method == "POST":
        fio = request.POST['fio']
        phone = request.POST['phone']
        company = request.POST.get('company', False)
        company_name = request.POST['company_name']
        inn = request.POST['inn']
        

        lead = Lead(fio = fio, phone = phone, company = company, company_name = company_name, inn = inn)
        lead.save()


        return redirect('base-home')
        


    context = {'discount': discount, 'lessons': lessons }
    return render(request, 'base/home.html', context)



