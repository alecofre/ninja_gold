from django.shortcuts import redirect, render,HttpResponse
import random
from datetime import datetime

# Create your views here.
def index(request):
     # return HttpResponse('iniciando el nija gold')
     if 'maximo' not in request.session:
          request.session['maximo'] = 10
     if 'gold' not in request.session:
          request.session['gold'] = 100
     if 'aleatorio' not in request.session:
          request.session['aleatorio'] = 'no'

     if 'oro_total' not in request.session or 'actividades' not in request.session:
          request.session['actividades'] = []
          request.session['turnos'] = 0

          if request.session['aleatorio'] == "si": 
               request.session['oro_total'] = random.randint(1,100)
          else:        
               request.session['oro_total'] = 0   

     return render(request,"index.html")

def process_money(request):
     if request.method == 'GET':
          return redirect('/')
     elif request.method == 'POST':
          if request.POST['gold'] == 'farm':
               oro = random.randint(10,20)
               request.session['actividades'].append(f'Has ganado {oro} monedas de oro en el campo!  ({ str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) } )')
          if request.POST['gold'] == 'cave':
               oro = random.randint(5,10)
               request.session['actividades'].append(f'Has ganado {oro} monedas de oro en la cueva!  ({ str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) } )')
          if request.POST['gold'] == 'house':
               oro = random.randint(2,5)
               request.session['actividades'].append(f'Has ganado {oro} monedas de oro en la casa!  ({ str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) } )')
          if request.POST['gold'] == 'casino':
               oro = random.randint(-50,50)
               if oro <=0:
                    suerte = 'perdido'
                    fichas = -oro
               else:
                    suerte = 'ganado'
                    fichas = oro
               request.session['actividades'].append(f'Has ido al casino y has {suerte} {fichas} monedas de oro!  ({ str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) } )')
          
          request.session['oro_total'] += oro
          request.session['turnos'] += 1

     if request.session['oro_total'] >= request.session['gold']:
          return render(request,'fin.html')
     
     if len(request.session['actividades']) >= request.session['maximo']:
          return render(request,'fin.html')

     return render(request,'index.html')


def play_again(request):
     request.session.flush()
     request.session['aleatorio'] = "no"
     request.session['maximo'] = 10
     request.session['gold'] = 100
     if request.method == "GET":
          pass
     elif request.method == "POST":          
          if  request.POST['aleatorio']  == 'si':
               request.session['aleatorio'] = "si"
          if request.POST['maximo'] == '20':
               request.session['maximo'] = 20
          if request.POST['gold'] == '200':
               request.session['gold'] = 200
     return redirect('/')