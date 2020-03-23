from django.shortcuts import render
from.models import EmpData
from.forms import EmpForm
from django.http.response import HttpResponse
def emp_view(request):
    if request.method=="POST":
        efrom=EmpForm(request.POST)
        if efrom.is_valid():
            ename1=request.POST.get('ename')
            sal1=request.POST.get('sal')
            email1=request.POST.get('email')
            mobile1=request.POST.get('mobile')
            location1=request.POST.get('location')
            data=EmpData(
                ename=ename1,
                sal=sal1,
                email=email1,
                mobile=mobile1,
                location=location1
            )
            data.save()
            efrom=EmpForm()
            context={'form':efrom}
            return render(request,'contact.html',context)
    else:
        eform=EmpForm()
        context={'form':eform}
        return render(request,'contact.html',context)

