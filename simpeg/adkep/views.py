from django.shortcuts import render, redirect
from adkep.models import Pegawai, Absen
from adkep.froms import FromPegawai, FromAbsen
from django.contrib import messages


# Create your views here.
def datapegawai(request):
    nama = Pegawai.objects.all()
    kontext = {
        'nama' : nama,
        
    }

    return render(request, 'pegawai.html', kontext)



def dataabsen(request):

    absen = Absen.objects.all()
    kontext = {
        'absen' : absen
    }

    return render(request, 'absen.html', kontext)





def tambah_pegawai(request):

    if request.POST:
       form = FromPegawai(request.POST) 
       if form.is_valid():
         form.save()
         pesan = "Data Berhasil Di Tambah"
         form = FromPegawai()
         kontext = {
             'form' : form,
             'pesan' : pesan,
         }
         return render(request, 'tambah-pegawai.html', kontext)  
    else:
        form = FromPegawai()

    kontext = {
        'form': form,
    }
    return render(request, 'tambah-pegawai.html', kontext)




def ubah_pegawai(request, id_pegawai):
   pegawai = Pegawai.objects.get(id=id_pegawai)
   templates = 'ubah-pegawai.html'
   if request.POST:
      form = FromPegawai(request.POST, instance=pegawai)
      if form.is_valid():
         form.save()
         messages.success(request, 'Data Berhasil diperbarui')
         return redirect('ubah_pegawai', id_pegawai=id_pegawai)
   else:
     form = FromPegawai(instance=pegawai)
     kontext = {
        'form':form,
        'pegawai':pegawai,
     }
     return render(request, templates, kontext) 
   
def hapus_pegawai(request, id_pegawai):
   pegawai = Pegawai.objects.filter(id=id_pegawai)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('datapegawai')




def tambah_absen(request):

    if request.POST:
       form = FromAbsen(request.POST) 
       if form.is_valid():
         form.save()
         pesan = "Data Berhasil Di Tambah"
         form = FromAbsen()
         kontext = {
             'form' : form,
             'pesan' : pesan,
         }
         return render(request, 'tambah-pegawai.html', kontext)  
    else:
        form = FromAbsen()

    kontext = {
        'form': form,
    }
    return render(request, 'tambah-absen.html', kontext)

def ubah_absen(request, id_absen):
   absen = Absen.objects.get(id=id_absen)
   templates = 'ubah-absen.html'
   if request.POST:
      form = FromAbsen(request.POST, instance=absen)
      if form.is_valid():
         form.save()
         messages.success(request, 'Data Berhasil diperbarui')
         return redirect('ubah_absen', id_absen=id_absen)
   else:
     form = FromPegawai(instance=absen)
     kontext = {
        'form':form,
        'absen':absen,
     }
     return render(request, templates, kontext) 
   
def hapus_absen(request, id_absen):
   absen = Absen.objects.filter(id=id_absen)
   absen.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('dataabsen')
