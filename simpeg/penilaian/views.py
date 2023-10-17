from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from adkep.models import PegawaiPekerjaan, PegawaiPribadi
from penilaian.models import Nilai
from penilaian.forms import FromNilai
from penilaian.resources import NilaiResource
from django.template.loader import get_template
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from openpyxl import Workbook



def check_access_superuser(user):
    if user.is_superuser or user.user_type == 'admin':
        return True
    return False


@login_required(login_url='login')
def nilai_user(request):
    today = timezone.now()
    current_month = today.strftime('%B')
    nilai = Nilai.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'], tanggal_penilaian__year=today.year, tanggal_penilaian__month=today.month)
    kontext = {
        'nilai' : nilai,
        'current_month' : current_month
    }

    return render(request, 'users/nilai-user.html', kontext)

class listPegawaiBawahan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

@login_required(login_url='login')
def nilai(request):
    today = timezone.now()
    jabatan_pengguna = request.user.jabatan
    bawahan = PegawaiPekerjaan.objects.filter(jabatan__atasan_id=jabatan_pengguna.id)
    current_month = today.strftime('%B')

    
    kontext = {
         'bawahan' : bawahan,
         'current_month' : current_month
        
    }
    print(bawahan)
    return render(request, 'nilai.html', kontext)

@login_required(login_url='login')
def detail_nilai(request,pegawaipribadi_id):
   
    today = timezone.now()
    nilai = Nilai.objects.filter(pegawaipribadi=pegawaipribadi_id)

    current_month = today.strftime('%B')


    kontext = {
        'nilai' : nilai,
        'current_month' : current_month
    }

    return render(request, 'detail-nilai.html', kontext)

@login_required(login_url='login')
def detail_nilai_user(request,pegawaipribadi_id):
   
    nilai = Nilai.objects.filter(pegawaipribadi=pegawaipribadi_id)
    
    kontext = {
        'nilai' : nilai,
    }

    return render(request, 'users/detail-nilai-user.html', kontext)

@login_required(login_url='login')
def edit_nilai(request, pegawaipribadi_id):
    pegawai = PegawaiPekerjaan.objects.get(pegawaipribadi=pegawaipribadi_id)
    current_month = timezone.now().month
    current_year = timezone.now().year

    try:
        existing_nilai = Nilai.objects.get(
            Q(pegawaipribadi=pegawaipribadi_id) &
            Q(tanggal_penilaian__month=current_month) &
            Q(tanggal_penilaian__year=current_year)
        )

        if request.method == 'POST':
            form = FromNilai(request.POST, instance=existing_nilai)
            if form.is_valid():
                nilai = form.save(commit=False)
                nilai.pegawaipribadi_id = pegawaipribadi_id
                
                # Menghitung rata-rata, nilai huruf, dan potongan
                total_nilai = (
                    int(nilai.kerapian) + int(nilai.kesopanan) + int(nilai.dedikasi) + int(nilai.loyalitas) +
                    int(nilai.disiplin) + int(nilai.kerjasama) + int(nilai.tupoksi)
                )
                jumlah_kriteria = 7  # Ganti dengan jumlah kriteria penilaian yang sesuai
                rata_rata = round(total_nilai / jumlah_kriteria)
                # Sisanya kode perhitungan seperti yang Anda lakukan sebelumnya
                
                nilai.rata_rata = rata_rata
                nilai.save()
                return redirect('edit_nilai', pegawaipribadi_id=pegawaipribadi_id)
        else:
            form = FromNilai(instance=existing_nilai)

        context = {
            'form': form,
            'pegawaipribadi_id': pegawaipribadi_id,
            'pegawai': pegawai,
        }
        return render(request, 'edit-nilai.html', context)

    except Nilai.DoesNotExist:
        # Jika nilai belum ada, Anda dapat mengarahkan pengguna ke halaman penambahan nilai baru
        return redirect('edit_nilai', pegawaipribadi_id=pegawaipribadi_id)


#tambah penilaian
@login_required(login_url='login')
def tambah_penilaian(request,pegawaipribadi_id):
    pegawai = PegawaiPekerjaan.objects.get(pegawaipribadi = pegawaipribadi_id)
    current_month = timezone.now().month
    current_year = timezone.now().year

    existing_nilai = Nilai.objects.filter(
        Q(pegawaipribadi=pegawaipribadi_id) &
        Q(tanggal_penilaian__month=current_month) &
        Q(tanggal_penilaian__year=current_year)
    )

    if existing_nilai.exists():
        existing_name = existing_nilai.first().pegawaipribadi.nama  # Replace 'nama' with the actual attribute name
        error_message = f"Penilaian untuk bulan ini sudah dilakukan untuk {existing_name}."
        messages.error(request, error_message)
        return redirect('nilai') 

    if request.method == 'POST':
        form = FromNilai(request.POST)
        if form.is_valid():
            nilai = form.save(commit=False)
            nilai.Pegawaipribadi = pegawai


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
            rata_rata = round(total_nilai / jumlah_kriteria)
            
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
            jumlah_potongan = min(total_nilai * (potongan / 100), 100)
            
            nilai.rata_rata = rata_rata
            nilai.nilai_huruf = nilai_huruf
            nilai.potongan = jumlah_potongan
            nilai.save()
            return redirect('tambah_nilai', pegawaipribadi_id=pegawaipribadi_id)
            
              # Ganti 'tambah_penilaian' dengan URL yang benar
        nilai.tanggal_penilaian = timezone.now()  # Set tanggal penilaian ke tanggal sekarang
        nilai.save()
        return redirect('daftar_nilai')  # Ganti dengan URL yang sesuai
    else:
        form = FromNilai()
    
    context = {
        'form': form,
        'pegawaipribadi_id': pegawaipribadi_id,
        'pegawai':pegawai
    }
    return render(request, 'tambah-nilai.html', context)


def tolakukur(request):
  
    kontext = {
        'tolakukur' : tolakukur,
        
    }

    return render(request, 'tolakukur.html', kontext)


@login_required(login_url='login')
def cetak_nilai(request, periode, pegawaipribadi_id):
   workbook = Workbook()
   sheet = workbook.active
   sheet.title = "Rekap Nilai"
   current_month = timezone.now().month 
   pegawai = Nilai.objects.filter(pegawaipribadi_id=pegawaipribadi_id)
   jabatan_pengguna = request.user.jabatan
   bawahan = PegawaiPekerjaan.objects.filter(jabatan__atasan_id= jabatan_pengguna.id).values_list('pegawaipribadi_id',flat=True)
  
   pegawai_bulan = Nilai.objects.filter(pegawaipribadi_id__in = bawahan )
   

   if periode == 'bulanan':
        current_month = timezone.now().month
        data_nilai = pegawai_bulan.filter(tanggal_penilaian__month=current_month, tanggal_penilaian__year=timezone.now().year)
   elif periode == 'semester':
        current_month = timezone.now().month

        # Filter untuk semester Maret - Agustus (bulan 3-8) -- smester ganjil
        if 3 <= current_month <= 8:
            data_nilai = pegawai.filter(tanggal_penilaian__month__range=[3, 8], tanggal_penilaian__year=timezone.now().year)

        # Filter untuk semester September - Februari (bulan 9-2) -- smester genap
        else:
            data_nilai = pegawai.filter(Q(tanggal_penilaian__month__gte=9) | Q(tanggal_penilaian__month__lte=2), tanggal_penilaian__year=timezone.now().year)
    # Menambahkan header ke baris pertama
   header = ['No', 'Nama', 'Total Nilai','Bulan','Potongan']
   sheet.append(header)

    # Menambahkan data nilai ke baris selanjutnya
   for idx, nilai in enumerate(data_nilai):
        row_data = [idx + 1, nilai.pegawaipribadi.nama, nilai.rata_rata,nilai.tanggal_penilaian.strftime('%B %Y'),nilai.potongan]
        sheet.append(row_data)

   response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
   response['Content-Disposition'] = f'attachment; filename=RekapNilai_{periode}.xlsx'
   workbook.save(response)

   return response
