from django.shortcuts import render
def home(request):
    return render(request,'accounts/index.html',{'param1':"KEERTHI"})