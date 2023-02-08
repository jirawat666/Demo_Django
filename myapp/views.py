from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"myapp/index.html",{})

def userreg(request):
    print("index",request)
    return render(request,"myapp/index.html",{})

def show_data(request):
    text = request.GET.get('text')
    return render(request, 'myapp/show_data.html', {'text': text})