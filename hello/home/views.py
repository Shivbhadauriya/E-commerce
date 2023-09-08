from django.shortcuts import render,HttpResponse

# Create your views here.
def frontpage(request):
    return render(request,"frontpage.html")
def grocery(request):
    return render(request,"grocery.html")
def mobile(request):
    return render(request,"mobile.html")
def footer(request):
    return render(request,"footer.css")
