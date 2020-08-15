from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Jop
from .form import Applyform , JopForm


# Create your views here.

def jop_list(request):
    jop_list = Jop.objects.all()
    paginator = Paginator(jop_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jops':page_obj }
    return render(request,'jop/jop_list.html',context)


def jop_detail(request , slug ):
    jop_detail = Jop.objects.get(slug=slug)

    if request.method == 'POST':
        form = Applyform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = jop_detail
            myform.save()
    else :
        form = Applyform() 

    context={'jop':jop_detail,'form':form}
    return render(request , 'jop/jop_detail.html',context)
    
def add_jop(request):

    if request.method == 'POST':
        form = JopForm(request.POST , request.FILES)
        if form.is_valid():
           myform = form.save(commit=False)
           myform.owner = request.user
           myform.save()
           return redirect(reverse('jops:jop_list'))
    
    else : 
        form = JopForm()

    context = {'form':form} 
    return render(request,'jop/add_jop.html',context)