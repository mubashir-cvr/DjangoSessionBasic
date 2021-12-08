from django.shortcuts import render

# Create your views here.
def index(request):
    if request.session.session_key==None:
        request.session.create()
    print(request.session.session_key)
    return render(request,'index.html')