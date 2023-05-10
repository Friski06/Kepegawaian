from django.shortcuts import render, redirect
from perizinan.models import Cutiizin, Spt
from perizinan.form import FromCuti, FromSpt
from django.contrib import messages


# Create your views here.
def cutiizin(request):
    cuti = Cutiizin.objects.all()
    kontext = {
        'cuti' : cuti,
        
    }

    return render(request, 'cutiizin.html', kontext)


def tambah_cutiizin(request):

    if request.POST:
       form = FromCuti(request.POST) 
       if form.is_valid():
         form.save()
         pesan = "Data Berhasil Di Tambah"
         form = FromCuti()
         kontext = {
             'form' : form,
             'pesan' : pesan,
         }
         return render(request, 'tambah-cuti.html', kontext)  
    else:
        form = FromCuti()

    kontext = {
        'form': form,
    }
    return render(request, 'tambah-cuti.html', kontext)

def ubah_cuti(request, id_cuti):
   cutiizin = Cutiizin.objects.get(id=id_cuti)
   templates = 'ubah-cuti.html'
   if request.POST:
      form = FromCuti(request.POST, instance=cutiizin)
      if form.is_valid():
         form.save()
         messages.success(request, 'Data Berhasil diperbarui')
         return redirect('ubah_cuti', id_cuti=id_cuti)
   else:
     form = FromCuti(instance=cutiizin)
     kontext = {
        'form':form,
        'cuti':cutiizin,
     }
     return render(request, templates, kontext) 
   
def hapus_cuti(request, id_cuti):
   pegawai = Cutiizin.objects.filter(id=id_cuti)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('cutiizin')








def spt(request):

    spt = Spt.objects.all()
    kontext = {
        'spt' : spt
    }

    return render(request, 'spt.html', kontext)

def tambah_spt(request):

    if request.POST:
       form = FromSpt(request.POST) 
       if form.is_valid():
         form.save()
         pesan = "Data Berhasil Di Tambah"
         form = FromSpt()
         kontext = {
             'form' : form,
             'pesan' : pesan,
         }
         return render(request, 'tambah-spt.html', kontext)  
    else:
        form = FromSpt()

    kontext = {
        'form': form,
    }
    return render(request, 'tambah-spt.html', kontext)

def ubah_spt(request, id_spt):
   spt = Spt.objects.get(id=id_spt)
   templates = 'ubah-spt.html'
   if request.POST:
      form = FromSpt(request.POST, instance=spt)
      if form.is_valid():
         form.save()
         messages.success(request, 'Data Berhasil diperbarui')
         return redirect('ubah_spt', id_spt=id_spt)
   else:
     form = FromCuti(instance=spt)
     kontext = {
        'form':form,
        'spt':spt,
     }
     return render(request, templates, kontext) 
   
def hapus_spt(request, id_spt):
   spt = Spt.objects.filter(id=id_spt)
   spt.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('spt')







