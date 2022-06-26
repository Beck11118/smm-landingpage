from django.shortcuts import render,redirect

from base.forms import LeadForm
from .models import Discount, Lesson

# Create your views here.

def home(request):

    discount = Discount.objects.get(id=1)
    lessons = Lesson.objects.all()

    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('base-home')
    
    else:
        form = LeadForm()
    


    context = {'discount': discount, 'lessons': lessons, 'form': form }
    return render(request, 'base/home.html', context)



