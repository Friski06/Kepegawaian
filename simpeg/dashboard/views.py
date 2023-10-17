from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from perizinan.models import Cutiizin
from adkep.models import PegawaiPekerjaan,JabatanBawahan

def is_admin(user):
    return user.is_superuser

@login_required(login_url='login')
def dashboard(request):
    cuti_izin_data = Cutiizin.objects.all()  # Sesuaikan query sesuai kebutuhan Anda
    return render(request, 'dashboard.html', {'cuti_izin_data': cuti_izin_data})

@user_passes_test(is_admin, login_url=settings.LOGIN_URL)
def tambah_jabatan(request, jabatan_id):
    jabatan = JabatanBawahan.objects.get(pk=jabatan_id)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_type = request.POST.get('user_type')

        user = User.objects.get(pk=user_id)
        user.user_type = user_type
        user.save()

        return redirect('list_jabatan')  # Ganti 'list_jabatan' dengan nama URL yang sesuai

    users = User.objects.all() 
    return render(request, 'tambah-jabatan.html', {'jabatan': jabatan, 'users': users})


def jumlahpegawai_tetap(request):
    jumlah_pegawai = PegawaiPekerjaan.objects.count()
    context = {'jumlah_pegawai': jumlah_pegawai}
    return render(request, 'dashboard.html', context)

