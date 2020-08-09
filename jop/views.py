from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Jop

# Create your views here.

def jop_list(request):
    jop_list = Jop.objects.all()
    paginator = Paginator(jop_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jops':page_obj}
    return render(request,'jop/jop_list.html',context)


def jop_detail(request , id ):
    jop_detail = Jop.objects.get(id = id)
    context={'jop':jop_detail}
    return render(request , 'jop/jop_detail.html',context)
    