from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from adkep.models import PegawaiPribadi, PegawaiPekerjaan, PegawaiPendidikan, PegawaiKeluarga, PegawaiBank
from adkep.froms import PegawaiPribadiForm, PegawaiPekerjaanForm, PegawaiPendidikanForm, PegawaiKeluargaForm, PegawaiBankForm
from django.contrib import messages


def check_access_superuser(user):
    if user.is_superuser or user.user_type == 'admin':
        return True
    return False

@login_required(login_url='login')

def pegawaipribadi_user(request):
        request.session['_auth_user_id']
        pegawai = PegawaiPribadi.objects.filter(user=request.user)
        konteks = {
            'pegawai' : pegawai,
        }

        return render(request, 'users/pegawaipribadi-user.html', konteks)


@login_required(login_url='login')
def pegawaipribadi(request):
    pegawai = PegawaiPribadi.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaipribadi.html', kontext)


@login_required(login_url='login')
def detail_pegawai_pribadi(request, id):
    pegawai = PegawaiPribadi.objects.filter(id=id)
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawaipribadi.html', kontext)


@login_required(login_url='login')
def tambah_pegawai_pribadi(request):
    if request.method == 'POST':
        form = PegawaiPribadiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_pribadi')
    else:
        form = PegawaiPribadiForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-pribadi.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_pribadi(request, id_pegawaipribadi):
    pegawai = PegawaiPribadi.objects.get(id=id_pegawaipribadi)
    if request.method == 'POST':
        form = PegawaiPribadiForm(request.POST, request.FILES, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaipribadi', id_pegawaipribadi=id_pegawaipribadi)
    else:
        form = PegawaiPribadiForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-pribadi.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_pribadi(request, id_pegawaipribadi):
   pegawai = PegawaiPribadi.objects.filter(id=id_pegawaipribadi)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipribadi')


#pegawaipekerjaan
@login_required(login_url='login')

def pegawaipekerjaan_user(request):
 
    pegawai = PegawaiPekerjaan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'users/pegawaipekerjaan-user.html', kontext)
 

@login_required(login_url='login')
def pegawaipekerjaan(request):
    pegawai = PegawaiPekerjaan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaipekerjaan.html', kontext)

@login_required(login_url='login')
def detail_pegawai_pekerjaan(request, id):
    pegawai = PegawaiPekerjaan.objects.filter(id=id)
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawaipekerjaan.html', kontext)

@login_required(login_url='login')
def tambah_pegawai_pekerjaan(request):
    if request.method == 'POST':
        form = PegawaiPekerjaanForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_pekerjaan')
    else:
        form = PegawaiPekerjaanForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-pekerjaan.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_pekerjaan(request, id_pegawaipekerjaan):
    pegawai = PegawaiPekerjaan.objects.get(id=id_pegawaipekerjaan)
    if request.method == 'POST':
        form = PegawaiPekerjaanForm(request.POST,request.FILES, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaipekerjaan', id_pegawaipekerjaan=id_pegawaipekerjaan)
    else:
        form = PegawaiPekerjaanForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-pekerjaan.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_pekerjaan(request, id_pegawaipekerjaan):
   pegawai = PegawaiPekerjaan.objects.filter(id=id_pegawaipekerjaan)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipekerjaan')

#pegawai pendidikan
@login_required(login_url='login')

def pegawaipendidikan_user(request):
  
    pegawai = PegawaiPendidikan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'users/pegawaipendidikan-user.html', kontext)
  

@login_required(login_url='login')
def pegawaipendidikan(request):
    pegawai = PegawaiPendidikan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaipendidikan.html', kontext)


@login_required(login_url='login')
def detail_pegawai_pendidikan(request):
    pegawai = PegawaiPendidikan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawai-pendidikan.html', kontext)

@login_required(login_url='login')
def tambah_pegawai_pendidikan(request):
    if request.method == 'POST':
        form = PegawaiPendidikanForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_pendidikan')
    else:
        form = PegawaiPendidikanForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-pendidikan.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_pendidikan(request, id_pegawaipendidikan):
    pegawai = PegawaiPendidikan.objects.get(id=id_pegawaipendidikan)
    if request.method == 'POST':
        form = PegawaiPendidikanForm(request.POST,request.FILES, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaipendidikan', id_pegawaipendidikan=id_pegawaipendidikan)
    else:
        form = PegawaiPendidikanForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-pendidikan.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_pendidikan(request, id_pegawaipendidikan):
   pegawai = PegawaiPendidikan.objects.filter(id=id_pegawaipendidikan)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipendidikan')

# pegawai keluarga
@login_required(login_url='login')

def pegawaikeluarga_user(request):
  
    pegawai = PegawaiKeluarga.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'users/pegawaikeluarga-user.html', kontext)
  

@login_required(login_url='login')
def pegawaikeluarga(request):
    pegawai = PegawaiKeluarga.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaikeluarga.html', kontext)



@login_required(login_url='login')
def detail_pegawai_keluarga(request):
    pegawai = PegawaiKeluarga.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawai-keluarga.html', kontext)

@login_required(login_url='login')
def tambah_pegawai_keluarga(request):
    if request.method == 'POST':
        form = PegawaiKeluargaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_keluarga')
    else:
        form = PegawaiKeluargaForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-keluarga.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_keluarga(request, id_pegawaikeluarga):
    pegawai = PegawaiKeluarga.objects.get(id=id_pegawaikeluarga)
    if request.method == 'POST':
        form = PegawaiKeluargaForm(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaikeluarga', id_pegawaikeluarga=id_pegawaikeluarga)
    else:
        form = PegawaiKeluargaForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-keluarga.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_keluarga(request, id_pegawaikeluarga):
   pegawai = PegawaiKeluarga.objects.filter(id=id_pegawaikeluarga)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaikeluarga')

#pegawai bank
@login_required(login_url='login')
def pegawaibank(request):
    pegawai = PegawaiBank.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaibank.html', kontext)

@login_required(login_url='login')
def detail_pegawai_bank(request):
  if check_access_superuser(request.user):
    pegawai = PegawaiBank.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawai-bank.html', kontext)

@login_required(login_url='login')
def tambah_pegawai_bank(request):
    if request.method == 'POST':
        form = PegawaiBankForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_bank')
    else:
        form = PegawaiBankForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-bank.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_bank(request, id_pegawaibank):
    pegawai = PegawaiBank.objects.get(id=id_pegawaibank)
    if request.method == 'POST':
        form = PegawaiBankForm(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaibank', id_pegawaibank=id_pegawaibank)
    else:
        form = PegawaiBankForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-bank.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_bank(request, id_pegawaibank):
   pegawai = PegawaiBank.objects.filter(id=id_pegawaibank)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaibank')

