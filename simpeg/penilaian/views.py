from django.shortcuts import render

def nilai(request):
  
    kontext = {
        'nilai' : nilai,
        
    }

    return render(request, 'nilai.html', kontext)

def tolakukur(request):
  
    kontext = {
        'tolakukur' : tolakukur,
        
    }

    return render(request, 'tolakukur.html', kontext)

