from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from absen.models import Absen, JabatanBawahan
from adkep.models import PegawaiPribadi
from absen.forms import AbsenForm
from django.contrib import messages
from decimal import Decimal
from django.db.models import Sum
from absen.resources import AbsenResource, AbsenUserResource
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.db.models import Q
from datetime import date
from django.utils import timezone
from openpyxl import Workbook



def check_access_superuser(user):
    if user.is_superuser or user.user_type == 'admin':
        return True
    return False


# Create your views here.

@login_required(login_url='login')
def absen_user(request):
    absen = Absen.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
    kontext = {
        'absen' : absen,
        
    }

    return render(request, 'users/absen-user.html', kontext)

#mengajukan keterlambatan absen ke admin
class listPegawaiBawahan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan 
@login_required(login_url='login')
def notifikasi_absen(request):
    
    absen = Absen.objects.all()
    belum = Absen.objects.filter(status = 'BELUM')
    print("ID Absen yang belum di-setujui:", [spt.id for spt in belum])
    kontext = {

         'belum'  : belum,
         'absen'  : absen
         
    }
    
    return render(request, 'notifikasi-absen.html',kontext)

def setuju_absen(request, id_absen):
    absen = Absen.objects.get(id=id_absen)
    
    if request.user.is_authenticated and request.user.user_type == 'admin':  # Pastikan pengguna adalah kaunit
        absen.status = 'DISETUJUI'
        absen.save()
        
    return redirect('notifikasi') 

def tolak_absen(request, id_absen):
    absen = Absen.objects.get(id=id_absen)
    
    if request.user.is_authenticated and request.user.user_type == 'admin':  # Pastikan pengguna adalah kaunit
        absen.status = 'DITOLAK'
        absen.save()
        
    return redirect('notifikasi')  


@login_required(login_url='login')
def absen(request):
    absen = Absen.objects.all()
    kontext = {
        'absen' : absen,
        
    }

    return render(request, 'absen.html', kontext)

@login_required(login_url='login')
def absen_bawahan(request):
    # Pastikan user yang sedang login memiliki atribut 'jabatan'
    try:
        jabatan_atasan = request.user.jabatan
    except AttributeError:
        jabatan_atasan = None

    # Cek jika user adalah atasan
    if jabatan_atasan and jabatan_atasan == 'atasan':
        # Mengambil data absen bawahan berdasarkan jabatan struktural
        absen_bawahan = Absen.objects.filter(jabatan__id_atasan=request.user.id)
    else:
        # Jika user bukan atasan, set data absen bawahan menjadi None
        absen_bawahan = None
    
    konteks = {
        'absen_bawahan': absen_bawahan,
    }
    
    return render(request, 'absen-bawahan.html', konteks)

@login_required(login_url='login')
def detailabsen(request):
    absen = Absen.objects.all()
    kontext = {
        'absen' : absen,
        
    }

    return render(request, 'detail-absen.html', kontext)

@login_required(login_url='login')
def lupaabsen(request):
    if request.method == 'POST':
        form = AbsenForm(request.POST)
        if form.is_valid():
            absen = form.save(commit=False)
            absen.pegawaipribadi = request.user.pegawaipribadi
            # Logika pengisian otomatis
            masuk = form.cleaned_data.get('masuk')
            pulang = form.cleaned_data.get('pulang')
            status = form.cleaned_data.get('status')
            if masuk and pulang:
                jam_masuk = masuk.hour * 60 + masuk.minute
                jam_pulang = pulang.hour * 60 + pulang.minute
                
                jumlah_jam = (jam_pulang - jam_masuk) / 60
                absen.jumlah_jam = round(jumlah_jam, 2)
                
                potongan_tukin = Decimal('0')
                
                if jam_masuk > 511:
                    if jam_masuk <= 526:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.005') * Decimal('0.5')
                    elif jam_masuk <= 541:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.01') * Decimal('1.0')
                    elif jam_masuk <= 556:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.015') * Decimal('1.5')
                    elif jam_masuk <= 571:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.02') * Decimal('2.0')
                    elif jam_masuk <= 586:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.025') * Decimal('2.5')
                
                if jam_pulang < 990:
                    if jam_pulang >= 900:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.025') * Decimal('2.5')
                    elif jam_pulang >= 885:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.02') * Decimal('2.0')
                    elif jam_pulang >= 870:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.015') * Decimal('1.5')
                    elif jam_pulang >= 855:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.01') * Decimal('1.0')
                    elif jam_pulang >= 840:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.005') * Decimal('0.5')

               

                absen.jumlah_potongan_tukin = round(potongan_tukin, 2)
                
                # Setelah semua perhitungan selesai, simpan data absen
                absen.save()
            return redirect('absen')
    else:
        form = AbsenForm(initial={'jumlah_jam':0, 'jumlah_potongan_tukin':0})
    
    konteks = {
        'form': form
    }
    return render(request, 'lupaabsen.html', konteks)


@login_required(login_url='login')
def rekap_absen_user(request):
    if request.method == 'POST':
        selected_month = int(request.POST.get('bulan'))  # Ambil bulan yang dipilih dari form
        absen_bulanan = Absen.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'], tanggal__month=selected_month)
        total_jumlah_tukin = absen_bulanan.aggregate(Sum('jumlah_potongan_tukin'))['jumlah_potongan_tukin__sum']
        total_jumlah_jam = absen_bulanan.aggregate(Sum('jumlah_jam'))['jumlah_jam__sum']
    else:
        absen_bulanan = Absen.objects.all()
        total_jumlah_tukin = absen_bulanan.aggregate(Sum('jumlah_potongan_tukin'))['jumlah_potongan_tukin__sum']
        total_jumlah_jam = absen_bulanan.aggregate(Sum('jumlah_jam'))['jumlah_jam__sum']

    konteks = {
       
        'absen_bulanan': absen_bulanan,
        'total_jumlah_tukin': total_jumlah_tukin,
        'total_jumlah_jam': total_jumlah_jam
    }
    return render(request, 'users/rekap-absen-user.html',konteks)


@login_required(login_url='login')
def rekap_absen_bulanan(request):
    if request.method == 'POST':
        selected_month = int(request.POST.get('bulan'))  # Ambil bulan yang dipilih dari form
        absen_bulanan = Absen.objects.filter(tanggal__month=selected_month)
        total_jumlah_tukin = absen_bulanan.aggregate(Sum('jumlah_potongan_tukin'))['jumlah_potongan_tukin__sum']
        total_jumlah_jam = absen_bulanan.aggregate(Sum('jumlah_jam'))['jumlah_jam__sum']
    else:
        absen_bulanan = Absen.objects.all()
        total_jumlah_tukin = absen_bulanan.aggregate(Sum('jumlah_potongan_tukin'))['jumlah_potongan_tukin__sum']
        total_jumlah_jam = absen_bulanan.aggregate(Sum('jumlah_jam'))['jumlah_jam__sum']

    konteks = {
       
        'absen_bulanan': absen_bulanan,
        'total_jumlah_tukin': total_jumlah_tukin,
        'total_jumlah_jam': total_jumlah_jam,
        

    }
    return render(request, 'rekap-absen-bulanan.html', konteks)

@login_required(login_url='login')
def detail_absen(request,pegawaipribadi_id):
    bulan = request.POST.get('bulan')
    
    try:
        selected_month = int(bulan)
    except (ValueError, TypeError):
        # Tangani jika nilai bulan tidak valid
        selected_month = None
    absen = Absen.objects.filter(pegawaipribadi=pegawaipribadi_id,tanggal__month=selected_month)
    total_jumlah_tukin = absen.aggregate(Sum('jumlah_potongan_tukin'))['jumlah_potongan_tukin__sum']
    total_jumlah_jam = absen.aggregate(Sum('jumlah_jam'))['jumlah_jam__sum']
    kontext = {
        'absen' : absen,
        'total_jumlah_tukin': total_jumlah_tukin,
        'total_jumlah_jam': total_jumlah_jam,
    }

    return render(request, 'detail-absen.html', kontext)

@login_required(login_url='login')
def cetak_rekap_absen(request,periode, pegawaipribadi_id):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Rekap Absen"
    current_month = timezone.now().month 
    pegawai = Absen.objects.filter(pegawaipribadi_id=pegawaipribadi_id)
    pegawai_bulan = Absen.objects.all()

    if periode == 'bulanan':
        current_month = timezone.now().month
        data_absen = pegawai_bulan.filter(tanggal__month=current_month, tanggal__year=timezone.now().year)
    elif periode == 'semester':
        current_month = timezone.now().month

        if 3 <= current_month <= 8:
            data_absen = pegawai.filter(tanggal__month__range=[3, 8], tanggal__year=timezone.now().year)
        else:
            data_absen = pegawai.filter(
                Q(tanggal__month__gte=9) | Q(tanggal__month__lte=2),
                tanggal__year=timezone.now().year,
            )

    # Menambahkan header ke baris pertama
    header = ['No','Nama','Tanggal', 'Potongan']
    sheet.append(header)

    # Menambahkan data absen ke baris selanjutnya
    for idx, absen in enumerate(data_absen):
        row_data = [idx + 1, absen.pegawaipribadi.nama ,absen.tanggal.strftime('%B %Y'), absen.jumlah_potongan_tukin]
        sheet.append(row_data)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=RekapAbsen_{periode}.xlsx'
    workbook.save(response)
    return response
  
@login_required(login_url='login')
def cetak_rekap_absen_user_pdf(request):
  
    pegawaipribadi = PegawaiPribadi.objects.first()
    absen = Absen.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])

    

    context = {
        'pegawaipribadi': pegawaipribadi,
        'absen' : absen,
        'exporting_pdf': True,
    }

    template = get_template('users/cetak-absen-user.html')
    html_content = template.render(context)

    pdf_buffer = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_buffer)

    if not pdf.err:
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Absen.pdf"'
        return response
    return HttpResponse('Error saat menghasilkan PDF', content_type='text/plain')


@login_required(login_url='login')
def cetak_rekap_absen_pdf(request):
  
    pegawaipribadi = PegawaiPribadi.objects.first()
    absen = Absen.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])

    

    context = {
        'pegawaipribadi': pegawaipribadi,
        'absen' : absen,
        'exporting_pdf': True,
    }

    template = get_template('cetak-absen.html')
    html_content = template.render(context)

    pdf_buffer = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_buffer)

    if not pdf.err:
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Absen.pdf"'
        return response
    return HttpResponse('Error saat menghasilkan PDF', content_type='text/plain')

