from django.shortcuts import render
from .utils import *

def index(request):
    if request.method=="GET":
       req_method="get"
       res=100
       return render(request,"spam.html",{"res":res,"req_method":req_method})
    elif request.method=="POST":
       sms=request.POST["sms"]
       res=classify(sms)
       req_method="POST"
       if res==0:
          res="NOT SPAM"
       else:
          res="SPAM"
       return render(request,"spam.html",{"res":res,"req_method":req_method})
