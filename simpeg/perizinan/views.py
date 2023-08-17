from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from perizinan.models import Cutiizin, Spt, Notifikasi
from django.contrib.auth.models import User
from perizinan.form import FromCuti, FromSpt
from django.contrib import messages
from login.models import User
from perizinan.resources import CutiResource
from django.template.loader import get_template
from xhtml2pdf import pisa


def check_access_superuser(user):
    if user.is_superuser or user.user_type == 'admin':
        return True
    return False


@login_required(login_url='login')
def cuti_user(request):
    cuti = Cutiizin.objects.filter(user_id=request.session['_auth_user_id'])
    kontext = {
        'cuti' : cuti,
        
    }

    return render(request, 'users/cutiizin-user.html', kontext)

class listPegawaiBawahan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
@login_required(login_url='login')
def notifikasi(request):
    jabatan_pengguna = request.user.jabatan
    bawahan = Cutiizin.objects.filter(jabatan__atasan_id=jabatan_pengguna.id)
    belum = Cutiizin.objects.filter(verifikasi_kaunit = 'BELUM')
    print("ID Cuti yang belum di-setujui:", [cuti.id for cuti in belum])
    kontext = {

         'belum'  : belum,
         'bawahan' : bawahan
         
    }
    print(bawahan)
    return render(request, 'notifikasi.html',kontext)

def setuju_cuti(request, id_cuti):
    cutiizin = Cutiizin.objects.get(id=id_cuti)
    
    if request.user.is_authenticated and request.user.user_type == 'kaunit':  # Pastikan pengguna adalah kaunit
        cutiizin.verifikasi_kaunit = 'DISETUJUI'
        cutiizin.save()
        
    return redirect('notifikasi')  

# Create your views here.
@login_required(login_url='login')
def cutiizin(request):
    cuti = Cutiizin.objects.all()
    kontext = {
        'cuti' : cuti,
        
    }

    return render(request, 'cutiizin.html', kontext)

@login_required(login_url='login')
def tambah_cutiizin(request):
   if request.method == 'POST':
        form = FromCuti(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tambah_cutiizin')
   else:
        form = FromCuti()
   context = {
        'form': form,
    }
   return render(request, 'tambah-cuti.html', context)


@login_required(login_url='login')
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
   

@login_required(login_url='login')
def detail_cuti(request,pegawaipribadi_id):
   
    cuti = Cutiizin.objects.filter(pegawaipribadi=pegawaipribadi_id)
   
    kontext = {
        'cuti' : cuti,
        
    }

    return render(request, 'detail-cuti.html', kontext)

@login_required(login_url='login')   
def hapus_cuti(request, id_cuti):
   pegawai = Cutiizin.objects.filter(id=id_cuti)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('cutiizin')

#cetak data
@login_required(login_url='login')
def cetak_rekap_cuti(request):
    
    cuti = CutiResource()
    dataset = cuti.export(queryset=Cutiizin.objects.filter(pegawaipribadi_id=request.session['_auth_user_id']))
    response = HttpResponse(dataset.xls, content_type= 'application/vnd.ms-excel' )
    response['Content-Disposition'] = 'attachment; filename=surat izin.xls'
    return response

@login_required(login_url='login')
def cetak_rekap_cuti_pdf(request):
   
   cuti_resource = CutiResource()
   queryset = Cutiizin.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
   dataset = cuti_resource.export(queryset=queryset)
    
   template_path = 'cetak-cuti.html'  # Ganti dengan path template HTML yang sesuai
   context = {'dataset': dataset}
    
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="surat izin.pdf"'
    
   template = get_template(template_path)
   html = template.render(context)
    
   pisa_status = pisa.CreatePDF(html, dest=response)
   if pisa_status.err:
        return HttpResponse('Gagal membuat PDF', content_type='text/plain')
    
   return response
#----akir cetak data----#




@login_required(login_url='login')
def spt_user(request):
    spt = Spt.objects.filter(user_id=request.session['_auth_user_id'])
    kontext = {
        'spt' : spt,
        
    }

    return render(request, 'users/spt-user.html', kontext)

class listPegawaiBawahan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

@login_required(login_url='login')
def notifikasi_spt(request):
    jabatan_pengguna = request.user.jabatan
    spt = Spt.objects.filter(jabatan__atasan_id=jabatan_pengguna.id)
    belum = Spt.objects.filter(status = 'BELUM')
    print("ID SPT yang belum di-setujui:", [spt.id for spt in belum])
    kontext = {

         'belum'  : belum,
         'spt' : spt
         
    }
    print(spt)
    return render(request, 'notifikasi-spt.html',kontext)

def setuju_spt(request, id_spt):
    spt = Spt.objects.get(id=id_spt)
    
    if request.user.is_authenticated and request.user.user_type == 'kaunit':  # Pastikan pengguna adalah kaunit
        spt.status = 'DISETUJUI'
        spt.save()
        
    return redirect('notifikasi_spt') 

def tolak_spt(request, id_spt):
    spt = Spt.objects.get(id=id_spt)
    
    if request.user.is_authenticated and request.user.user_type == 'kaunit':  # Pastikan pengguna adalah kaunit
        spt.status = 'DITOLAK'
        spt.save()
        
    return redirect('notifikasi_spt')  

@login_required(login_url='login')
def spt(request):

    spt = Spt.objects.all()
    kontext = {
        'spt' : spt
    }

    return render(request, 'spt.html', kontext)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')   
def hapus_spt(request, id_spt):
   spt = Spt.objects.filter(id=id_spt)
   spt.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('spt')





