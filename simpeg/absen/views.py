from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from absen.models import Absen
from absen.forms import AbsenForm
from django.contrib import messages
from decimal import Decimal
from django.db.models import Sum
import datetime

def check_access_superuser(user):
    if user.is_superuser or user.user_type == 'kaunit':
        return True
    return False


# Create your views here.

@login_required(login_url='login')
def absen_user(request):
    absen = Absen.objects.all()
    kontext = {
        'absen' : absen,
        
    }

    return render(request, 'users/absen-user.html', kontext)


@login_required(login_url='login')
def absen(request):
    absen = Absen.objects.all()
    kontext = {
        'absen' : absen,
        
    }

    return render(request, 'absen.html', kontext)

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
            
            # Logika pengisian otomatis
            masuk = form.cleaned_data.get('masuk')
            pulang = form.cleaned_data.get('pulang')
            
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
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.005') * Decimal('1.0')
                    elif jam_masuk <= 556:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.005') * Decimal('1.5')
                    elif jam_masuk <= 571:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.005') * Decimal('2.0')
                    elif jam_masuk <= 586:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.005') * Decimal('2.5')
                
                if jam_pulang < 990:
                    if jam_pulang >= 975:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.025') * Decimal('2.5')
                    elif jam_pulang >= 960:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.025') * Decimal('2.0')
                    elif jam_pulang >= 945:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.025') * Decimal('1.5')
                    elif jam_pulang >= 930:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.025') * Decimal('1.0')
                    elif jam_pulang >= 915:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.025') * Decimal('0.5')
                    elif jam_pulang >= 890:
                        potongan_tukin += Decimal(jumlah_jam) * Decimal('0.025') * Decimal('0.25')
                
                absen.jumlah_potongan_tukin = round(potongan_tukin, 2)
            
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
    # Mengambil data absen bulanan
    absen_bulanan = Absen.objects.filter(tanggal__year=datetime.date.today().year)
    
    # Menghitung total jumlah tukin dan jumlah jam
    total_jumlah_tukin = absen_bulanan.aggregate(Sum('jumlah_potongan_tukin'))['jumlah_potongan_tukin__sum']
    total_jumlah_jam = absen_bulanan.aggregate(Sum('jumlah_jam'))['jumlah_jam__sum']
    
    konteks = {
        'absen_bulanan': absen_bulanan,
        'total_jumlah_tukin': total_jumlah_tukin,
        'total_jumlah_jam': total_jumlah_jam
    }
    
    return render(request, 'users/rekap-absen-user.html', konteks)


@login_required(login_url='login')
def rekap_absen_bulanan(request):
    # Mengambil data absen bulanan
    absen_bulanan = Absen.objects.filter(tanggal__year=datetime.date.today().year)
    
    # Menghitung total jumlah tukin dan jumlah jam
    total_jumlah_tukin = absen_bulanan.aggregate(Sum('jumlah_potongan_tukin'))['jumlah_potongan_tukin__sum']
    total_jumlah_jam = absen_bulanan.aggregate(Sum('jumlah_jam'))['jumlah_jam__sum']
    
    konteks = {
        'absen_bulanan': absen_bulanan,
        'total_jumlah_tukin': total_jumlah_tukin,
        'total_jumlah_jam': total_jumlah_jam
    }
    
    return render(request, 'rekap-absen-bulanan.html', konteks)
