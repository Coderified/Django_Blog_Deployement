from django.shortcuts import render
from Whats_CARE.models import links 

# Create your views here.
def Carebasic(request):
    return render(request, 'Carebase.html',)

def basicview(request):
    titlelinks = links.objects.all()
    context={
        'titlelinks':titlelinks
    }
    return render(request, 'titlelinks.html',context)

def detailview(request,pk):
    detaillink = links.objects.get(pk=pk)
    context={
        'detaillink':detaillink
    }
    return render(request,'detaillink.html',context)



