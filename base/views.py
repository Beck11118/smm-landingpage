from django.shortcuts import render,redirect
from django.contrib import messages

from base.forms import LeadForm
from .models import Discount, Lesson, Lead

# Create your views here.

def home(request):

    discount = Discount.objects.get(id=1)
    lessons = Lesson.objects.all()

    
    if request.method == "POST":
        
        if request.POST['phone'] != "" or request.POST['fio'] != "":
            phone = request.POST['phone']
            fio = request.POST['fio']
        if request.POST['phone'] == "" or request.POST['fio'] == "": 
            messages.error(request, "Iltimos bo'sh joyni to'ldiring")
            return redirect('base-home')     
        company = request.POST.get('company', False)
        company_name = request.POST['company_name']
        
        if request.POST['inn'] != "":inn = request.POST['inn']
        else: inn = None

        lead = Lead(fio = fio, phone = phone, company = company, company_name = company_name, inn = inn)
        lead.save()
        messages.success(request, "Sizning so'rovnomangiz muvaffaqiyatli jo'natildi")

        return redirect('base-home')
        


    context = {'discount': discount, 'lessons': lessons, }
    return render(request, 'base/home.html', context)

def lead(request):
    if request.method == "POST":
        fio = request.POST['fio']
        if request.POST['phone'] != "":phone = request.POST['phone']
        else: phone = None
        company = request.POST.get('company', False)
        company_name = request.POST['company_name']
        
        if request.POST['inn'] != "":inn = request.POST['inn']
        else: inn = None

        lead = Lead(fio = fio, phone = phone, company = company, company_name = company_name, inn = inn)
        lead.save()
        messages.success(request, "Sizning so'rovnomangiz muvaffaqiyatli jo'natildi")

        return redirect('base-home')





