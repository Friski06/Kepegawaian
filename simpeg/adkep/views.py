from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from adkep.models import PegawaiPribadi, PegawaiPekerjaan, PegawaiPendidikan, PegawaiKeluarga, PegawaiBank, JabatanBawahan, JabtanAtasan
from adkep.froms import PegawaiPribadiForm, PegawaiPekerjaanForm, PegawaiPendidikanForm, PegawaiKeluargaForm, PegawaiBankForm
from django.contrib import messages
from django.contrib.auth.models import User

def check_access_superuser(user):
    if user.is_superuser or user.user_type == 'admin':
        return True
    return False

@login_required(login_url='login')

def pegawaipribadi_user(request):
        pegawai = PegawaiPribadi.objects.filter(user_id=request.session['_auth_user_id'])
        konteks = {
            'pegawai' : pegawai,
        }

        return render(request, 'users/pegawaipribadi-user.html', konteks)

class listPegawaiBawahan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

@login_required(login_url='login')
def pegawaibawahan(request):
    jabatan_pengguna = request.user.jabatan
    bawahan = PegawaiPekerjaan.objects.filter(jabatan__atasan_id=jabatan_pengguna.id)
    
    """
    data = []
    for bawahan in bawahan:
    #  print("id pada jabatanbawahan " + str(bawahan.id) + "--" + str(bawahan.nama_jabatan))
     pekerjaan = PegawaiPekerjaan.objects.filter(jabatan_id=bawahan.id)
     for kerja in pekerjaan:
        # print("\tid pada pegawaipekerjaan " + str(kerja.id))
        datapegawai = PegawaiPribadi.objects.filter(user_id = kerja.pegawaipribadi_id)
        for pegawai in datapegawai:
            # print("\t\tuser_id pada pegawaipribadi " + str(pegawai.user_id))
            print("\tnama  pegawai " + str(pegawai.nama))
            # print(str(pegawai.nama) + str(bawahan.nama_jabatan))
            data.append(listPegawaiBawahan(pegawai.nama,bawahan.nama_jabatan))
     """
    kontext = {
         'bawahan' : bawahan,
        
    }
    print(bawahan)
    return render(request, 'users/databawahan.html', kontext)


@login_required(login_url='login')
def pegawaipribadi(request):
    pegawai = PegawaiPribadi.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaipribadi.html', kontext)


@login_required(login_url='login')
def detail_pegawai_pribadi(request, user_id):
    pegawai = PegawaiPribadi.objects.filter(user_id=user_id)
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawaipribadi.html', kontext)


@login_required(login_url='login')
def tambah_pegawai_pribadi(request):
    if request.method == 'POST':
        form = PegawaiPribadiForm(request.POST, request.FILES)
        if form.is_valid():
            pegawai = form.save(commit=False)  # Tambahkan parameter commit=False untuk sementara
            pegawai.user = request.user  # Set nilai user dengan user yang sedang login
            pegawai.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_pribadi')
    else:
        form = PegawaiPribadiForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-pribadi.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_pribadi(request, user_id):
    pegawai = PegawaiPribadi.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = PegawaiPribadiForm(request.POST, request.FILES, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaipribadi', user_id=user_id)
    else:
        form = PegawaiPribadiForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-pribadi.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_pribadi(request, user_id):
   pegawai = PegawaiPribadi.objects.filter(user_id=user_id)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipribadi')


#pegawaipekerjaan
@login_required(login_url='login')

def pegawaipekerjaan_user(request):
  pekerjaan = PegawaiPekerjaan.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
  konteks = {
            'pekerjaan' : pekerjaan,
        }
  return render(request, 'users/pegawaipekerjaan-user.html', konteks)
 

@login_required(login_url='login')
def pegawaipekerjaan(request):
    pekerjaan = PegawaiPekerjaan.objects.all()
    kontext = {
        'pekerjaan' : pekerjaan,
        
    }

    return render(request, 'pegawaipekerjaan.html', kontext)

@login_required(login_url='login')
def detail_pegawai_pekerjaan(request, user_id):
    pegawai = PegawaiPekerjaan.objects.filter(id=user_id)
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawaipekerjaan.html', kontext)

@login_required(login_url='login')
def tambah_pegawai_pekerjaan(request):
    if request.method == 'POST':
        form = PegawaiPekerjaanForm(request.POST, request.FILES)
        if form.is_valid():
            pegawai = form.save(commit=False)  # Tambahkan parameter commit=False untuk sementara
            pegawai.pegawaipribadi = request.user.pegawaipribadi  # Set nilai user dengan user yang sedang login
            pegawai.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_pekerjaan')
    else:
        form = PegawaiPekerjaanForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-pekerjaan.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_pekerjaan(request, user_id):
    pegawai = PegawaiPekerjaan.objects.get(id=user_id)
    if request.method == 'POST':
        form = PegawaiPekerjaanForm(request.POST,request.FILES, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaipekerjaan', user_id=user_id)
    else:
        form = PegawaiPekerjaanForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-pekerjaan.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_pekerjaan(request, user_id):
   pegawai = PegawaiPekerjaan.objects.filter(id=user_id)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipekerjaan')

#pegawai pendidikan
@login_required(login_url='login')

def pegawaipendidikan_user(request):
  
    pendidikan = PegawaiPendidikan.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
    kontext = {
        'pendidikan' : pendidikan,
        
    }

    return render(request, 'users/pegawaipendidikan-user.html', kontext)
  

@login_required(login_url='login')
def pegawaipendidikan(request):
    pegawai_pendidikan = PegawaiPendidikan.objects.all()
    kontext = {
        'pendidikan' : pegawai_pendidikan,
        
    }

    return render(request, 'pegawaipendidikan.html', kontext)


@login_required(login_url='login')
def detail_pegawai_pendidikan(request, user_id):
    pegawai = PegawaiPendidikan.objects.filter(id=user_id)
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawai-pendidikan.html', kontext)

@login_required(login_url='login')
def tambah_pegawai_pendidikan(request):
    if request.method == 'POST':
        form = PegawaiPendidikanForm(request.POST, request.FILES)
        if form.is_valid():
            pegawai = form.save(commit=False)  # Tambahkan parameter commit=False untuk sementara
            pegawai.pegawaipribadi = request.user.pegawaipribadi  # Set nilai user dengan user yang sedang login
            pegawai.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_pendidikan')
    else:
        form = PegawaiPendidikanForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-pendidikan.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_pendidikan(request, user_id):
    pegawai = PegawaiPendidikan.objects.get(id=user_id)
    if request.method == 'POST':
        form = PegawaiPendidikanForm(request.POST,request.FILES, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaipendidikan', user_id=user_id)
    else:
        form = PegawaiPendidikanForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-pendidikan.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_pendidikan(request, user_id):
   pegawai = PegawaiPendidikan.objects.filter(id=user_id)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipendidikan')

# pegawai keluarga
@login_required(login_url='login')

def pegawaikeluarga_user(request):
  
    keluarga = PegawaiKeluarga.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
    kontext = {
        'keluarga' : keluarga,
        
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
def detail_pegawai_keluarga(request, user_id):
    pegawai = PegawaiKeluarga.objects.filter(id=user_id)
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawai-keluarga.html', kontext)

@login_required(login_url='login')
def tambah_pegawai_keluarga(request):
    if request.method == 'POST':
        form = PegawaiKeluargaForm(request.POST, request.FILES)
        if form.is_valid():
            pegawai = form.save(commit=False)  # Tambahkan parameter commit=False untuk sementara
            pegawai.pegawaipribadi = request.user.pegawaipribadi  # Set nilai user dengan user yang sedang login
            pegawai.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('tambah_pegawai_keluarga')
    else:
        form = PegawaiKeluargaForm()

    konteks = {
        'form': form,
    }
    return render(request, 'tambah-pegawai-keluarga.html', konteks)

@login_required(login_url='login')
def ubah_pegawai_keluarga(request, user_id):
    pegawai = PegawaiKeluarga.objects.get(id=user_id)
    if request.method == 'POST':
        form = PegawaiKeluargaForm(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_pegawaikeluarga', user_id=user_id)
    else:
        form = PegawaiKeluargaForm(instance=pegawai)

    konteks = {
        'form': form,
        'pegawai': pegawai,
    }
    return render(request, 'ubah-pegawai-keluarga.html', konteks)

@login_required(login_url='login')
def hapus_pegawai_keluarga(request, user_id):
   pegawai = PegawaiKeluarga.objects.filter(id=user_id)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaikeluarga')

#pegawai bank

@login_required(login_url='login')
def pegawaibank_user(request):
    pegawai = PegawaiBank.objects.filter(pegawaipribadi_id=request.session['_auth_user_id'])
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'users/pegawaibank-user.html', kontext)


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
        form = PegawaiBankForm(request.POST, request.FILES)
        if form.is_valid():
            pegawai = form.save(commit=False)  # Tambahkan parameter commit=False untuk sementara
            pegawai.pegawaipribadi = request.user.pegawaipribadi  # Set nilai user dengan user yang sedang login
            pegawai.save()
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

