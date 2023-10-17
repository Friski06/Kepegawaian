from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from perizinan.models import Cutiizin, Spt, Notifikasi, Upload_Spt
from adkep.models import PegawaiPribadi
from django.contrib.auth.models import User
from perizinan.form import FromCuti, FromSpt,SptUploadForm
from django.contrib import messages
from login.models import User
from perizinan.resources import CutiResource
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.utils import timezone
from openpyxl import Workbook
from django.db.models import Q
from datetime import date



def check_access_superuser(user):
    if user.is_superuser or user.user_type == 'admin':
        return True
    return False


@login_required(login_url='login')
def cuti_user(request):
    cuti = Cutiizin.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
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
            cuti = form.save(commit=False)  # Tambahkan parameter commit=False untuk sementara
            cuti.pegawaipribadi = request.user.pegawaipribadi
            # Set tgl_mulai and tgl_selesai fields before saving the form
            tgl_mulai = form.cleaned_data['tgl_mulai']
            tgl_selesai = form.cleaned_data['tgl_selesai']
            form.instance.tgl_mulai = tgl_mulai
            form.instance.tgl_selesai = tgl_selesai

            # Save the form
            cuti.save()
            return redirect('tambah_cutiizin')
   else:
        form = FromCuti(initial={'hari':0})
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
   
   pegawaipribadi = PegawaiPribadi.objects.first()
   cuti = Cutiizin.objects.all()

    

   context = {
        'pegawaipribadi': pegawaipribadi,
        'cuti' : cuti,
        'exporting_pdf': True,
    }

   template = get_template('cetak-cuti.html')
   html_content = template.render(context)

   pdf_buffer = BytesIO()
   pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_buffer)

   if not pdf.err:
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="cuti.pdf"'
        return response
   return HttpResponse('Error saat menghasilkan PDF', content_type='text/plain')

#----akir cetak data----#

@login_required(login_url='login')
def cetak_user_cuti_pdf(request):
   
   pegawaipribadi = PegawaiPribadi.objects.get(user=request.user)  # Mengambil pegawai yang sesuai dengan pengguna yang sedang login
   cuti = Cutiizin.objects.filter(pegawaipribadi=pegawaipribadi)

    

   context = {
        'pegawaipribadi': pegawaipribadi,
        'cuti' : cuti,
        'exporting_pdf': True,
    }

   template = get_template('cetak-cuti.html')
   html_content = template.render(context)

   pdf_buffer = BytesIO()
   pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_buffer)

   if not pdf.err:
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="cuti.pdf"'
        return response
   return HttpResponse('Error saat menghasilkan PDF', content_type='text/plain')

#----akir cetak data----#


# Rekap Cuti User

@login_required(login_url='login')
def rekap_cuti_user(request,pegawaipribadi_id):
   
    cuti = Cutiizin.objects.filter(pegawaipribadi=pegawaipribadi_id)
   
    kontext = {
        'cuti' : cuti,
        
    }

    return render(request, 'users/rekap-cuti.html', kontext)


@login_required(login_url='login')
def cetak_cuti(request, periode, pegawaipribadi_id):
   workbook = Workbook()
   sheet = workbook.active
   sheet.title = "Rekap Cuti"
   current_month = timezone.now().month 
   pegawai = Cutiizin.objects.filter(pegawaipribadi_id=pegawaipribadi_id)
   pegawai_bulan = Cutiizin.objects.filter(pegawaipribadi_id=pegawaipribadi_id)

   if periode == 'bulanan':
        current_month = timezone.now().month
        data_nilai = pegawai_bulan.filter(tgl_mulai__month=current_month, tgl_mulai__year=timezone.now().year)
   elif periode == 'semester':
        current_month = timezone.now().month

        # Filter untuk semester Maret - Agustus (bulan 3-8) -- smester ganjil
        if 3 <= current_month <= 8:
            data_nilai = pegawai.filter(tgl_mulai__month__range=[3, 8], tgl_mulai__year=timezone.now().year)

        # Filter untuk semester September - Februari (bulan 9-2) -- smester genap
        else:
            data_nilai = pegawai.filter(Q(tgl_mulai__month__gte=9) | Q(tgl_mulai__month__lte=2), tgl_mulai__year=timezone.now().year)
    # Menambahkan header ke baris pertama
   header = ['No', 'Nama', 'Keperluan','Tanggal Mulai','Tanggal Selesai']
   sheet.append(header)

    # Menambahkan data nilai ke baris selanjutnya
   for idx, cuti in enumerate(data_nilai):
        row_data = [idx + 1, cuti.pegawaipribadi.nama, cuti.keperluan,cuti.tgl_mulai.strftime('%B %Y'),cuti.tgl_selesai.strftime('%B %Y')]
        sheet.append(row_data)

   response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
   response['Content-Disposition'] = f'attachment; filename=RekapNilai_{periode}.xlsx'
   workbook.save(response)

   return response


# Akir Cuti




@login_required(login_url='login')
def spt_user(request):
    spt = Spt.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
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
def upload_spt(request):
    if request.method == 'POST':
        form = SptUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('spt')  # Ganti dengan halaman yang sesuai
    else:
     form = SptUploadForm()
    return render(request, 'upload-spt.html', {'form': form})
    

@login_required(login_url='login')
def detail_spt(request,spt_id):
   
    spt = get_object_or_404(Spt, pk=spt_id)
    upload_spt = spt.spt
    return render(request, 'detail-spt.html', {'spt': spt, 'upload_spt': upload_spt})

@login_required(login_url='login')
def tambah_spt(request):
    if request.method == 'POST':
        form = FromSpt(request.POST)
        current_month = timezone.now().day
        if form.is_valid():
            spt = form.save(commit=False)
            # Ambil semua nama dan nip yang diisi dalam list
            nama_list = request.POST.getlist('nama[]')
            nip_list = request.POST.getlist('nip[]')

            # Gabungkan semua nilai dalam list menjadi satu teks (dalam contoh ini, dipisahkan oleh koma)
            spt.pegawai_nama = ', '.join(nama_list)
            spt.pegawai_nip = ', '.join(nip_list)
            if not spt.pegawai_nama or not spt.pegawai_nip:
                # Jika nama atau NIP tidak diisi, gunakan nama dan NIP pengguna yang mengajukan
                spt.pegawai_nama = request.user.pegawaipribadi.nama
                spt.pegawai_nip = request.user.pegawaipribadi.nip
            spt.pegawaipribadi = request.user.pegawaipribadi
            spt.save()
            spt.tanggal_pengajuan = timezone.now()
            pesan = "Data Berhasil Di Tambah"
            form = FromSpt()
            kontext = {
                'spt': spt,
                'pesan': pesan,
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





