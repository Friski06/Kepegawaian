from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from perizinan.form import JabatanForm
from django.contrib import messages
from adkep.models import PegawaiPekerjaan

def is_admin(user):
    return user.is_superuser

@login_required(login_url='login')
def dashboard(request):
    kontext = {}
    return render(request, 'dashboard.html', kontext)

@user_passes_test(is_admin, login_url=settings.LOGIN_URL)
def tambah_jabatan(request):
    if request.method == 'POST':
        form = JabatanForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_jabatan')
    else:
        form = JabatanForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-jabatan.html', konteks)


def jumlahpegawai_tetap(request):
    jumlah_pegawai = PegawaiPekerjaan.objects.count()
    context = {'jumlah_pegawai': jumlah_pegawai}
    return render(request, 'dashboard.html', context)

