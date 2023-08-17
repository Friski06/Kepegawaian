from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from adkep.models import PegawaiPekerjaan, PegawaiPribadi
from penilaian.models import Nilai
from penilaian.forms import FromNilai
from penilaian.resources import NilaiResource
from django.template.loader import get_template


def check_access_superuser(user):
    if user.is_superuser or user.user_type == 'admin':
        return True
    return False


@login_required(login_url='login')
def nilai_user(request):
    nilai = Nilai.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
    kontext = {
        'nilai' : nilai,
        
    }

    return render(request, 'users/nilai-user.html', kontext)

class listPegawaiBawahan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

@login_required(login_url='login')
def nilai(request):
    jabatan_pengguna = request.user.jabatan
    bawahan = PegawaiPekerjaan.objects.filter(jabatan__atasan_id=jabatan_pengguna.id)

    kontext = {
         'bawahan' : bawahan,
        
    }
    print(bawahan)
    return render(request, 'nilai.html', kontext)

@login_required(login_url='login')
def detail_nilai(request,pegawaipribadi_id):
   
    nilai = Nilai.objects.filter(pegawaipribadi=pegawaipribadi_id)
    
    kontext = {
        'nilai' : nilai,
    }

    return render(request, 'detail-nilai.html', kontext)

@login_required(login_url='login')
def detail_nilai_user(request,pegawaipribadi_id):
   
    nilai = Nilai.objects.filter(pegawaipribadi=pegawaipribadi_id)
    
    kontext = {
        'nilai' : nilai,
    }

    return render(request, 'users/detail-nilai-user.html', kontext)

#tambah penilaian
@login_required(login_url='login')
def tambah_penilaian(request,pegawaipribadi_id):
    pegawai = PegawaiPekerjaan.objects.get(pegawaipribadi = pegawaipribadi_id)
    
    if request.method == 'POST':
        form = FromNilai(request.POST)
        if form.is_valid():
            nilai = form.save(commit=False)
            nilai.pegawaipribadi_id = pegawaipribadi_id 

            # Menghitung rata-rata
            total_nilai = (
                int(nilai.kerapian) + int(nilai.kesopanan) + int(nilai.dedikasi) + int(nilai.loyalitas) +
                int(nilai.disiplin) + int(nilai.kerjasama) + int(nilai.tupoksi)
            )
            jumlah_kriteria = 7  # Ganti dengan jumlah kriteria penilaian yang sesuai
            rata_rata = round(total_nilai / jumlah_kriteria, 1)
            
            # Menghitung nilai huruf
            if rata_rata >= 81:
                nilai_huruf = 'A'
                potongan = 0
            elif rata_rata >= 71:
                nilai_huruf = 'B'
                potongan = 0
            elif rata_rata >= 61:
                nilai_huruf = 'C'
                potongan = 1
            elif rata_rata >= 51:
                nilai_huruf = 'D'
                potongan = 75
            else:
                nilai_huruf = 'E'
                potongan = 100
            
            # Menghitung jumlah potongan
            jumlah_potongan = total_nilai * (potongan / 100)
            
            nilai.rata_rata = rata_rata
            nilai.nilai_huruf = nilai_huruf
            nilai.potongan = jumlah_potongan
            nilai.save()
            return redirect('tambah_nilai', pegawaipribadi_id=pegawaipribadi_id)
            
              # Ganti 'tambah_penilaian' dengan URL yang benar
    else:
        form = FromNilai()
    
    context = {
        'form': form,
        'pegawaipribadi_id': pegawaipribadi_id,
    }
    return render(request, 'tambah-nilai.html', context)


def tolakukur(request):
  
    kontext = {
        'tolakukur' : tolakukur,
        
    }

    return render(request, 'tolakukur.html', kontext)


@login_required(login_url='login')
def cetak_nilai(request):
    
    nilai = NilaiResource()
    dataset = nilai.export(queryset=Nilai.objects.filter(pegawaipribadi_id=request.session['_auth_user_id']))
    response = HttpResponse(dataset.xls, content_type= 'application/vnd.ms-excel' )
    response['Content-Disposition'] = 'attachment; filename=nilai.xls'
    return response