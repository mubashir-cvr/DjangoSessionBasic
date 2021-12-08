from django.shortcuts import render

# Create your views here.
def index(request):
    if request.session.session_key==None:
        request.session.create()
        context={
            'created':request.session.session_key
        }
        return render(request,'index.html',context)
    context={
            'previous':request.session.session_key
        }
    return render(request,'index.html',context)