from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.
def home(request):  
    if request.method=="POST":
        formed=formsdata(request.POST,request.FILES)
        if formed.is_valid():
            formed.save()
            return HttpResponseRedirect("candidates")    
    else:
        formed=formsdata()  
    return render(request,"main.html",{"formed":formed})





def resumeviwer(request,pk):
    data=resumedata.objects.get(pk=pk)
   
    
    return render(request,"resume_page.html",{"data":data})





def showcandidates(request):
    candidates=resumedata.objects.all()
    return render(request,"candidates.html",{"candidates":candidates})




# def resumeviwer(request):
#     data=resumedata.objects.all().order_by('-id').first()
    
    # return render(request,"resume_page.html",{"data":data})