from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "operation" : "null",
        }
    return render(request,'calculator.html', context= context)

#Recive la informacion del post
def submitquery(request):

    #al intentar recojer informacion de un input podemos saber si la informacion es valida o no
    try:
        A = int(request.GET['queryA'])
    except:
        A = 0
    
    try:
        B = int(request.GET['queryB'])
    except:
        B = 0

    operation = A + B

    #Devolvemos la informacion en formato JSON y la devolvemos a la web
    context = {
        "operation" : operation,
               }
    return render(request,'calculator.html', context)
