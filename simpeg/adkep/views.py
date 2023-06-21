from django.shortcuts import render, redirect
from adkep.models import PegawaiPribadi, PegawaiPekerjaan, PegawaiPendidikan, PegawaiKeluarga, PegawaiBank
from adkep.froms import PegawaiPribadiForm, PegawaiPekerjaanForm, PegawaiPendidikanForm, PegawaiKeluargaForm, PegawaiBankForm
from django.contrib import messages

def pegawaipribadi(request):
    pegawai = PegawaiPribadi.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaipribadi.html', kontext)

def detail_pegawai_pribadi(request, id):
    pegawai = PegawaiPribadi.objects.filter(id=id)
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawaipribadi.html', kontext)


def tambah_pegawai_pribadi(request):
    if request.method == 'POST':
        form = PegawaiPribadiForm(request.POST)
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

def ubah_pegawai_pribadi(request, id_pegawaipribadi):
    pegawai = PegawaiPribadi.objects.get(id=id_pegawaipribadi)
    if request.method == 'POST':
        form = PegawaiPribadiForm(request.POST, instance=pegawai)
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

def hapus_pegawai_pribadi(request, id_pegawaipribadi):
   pegawai = PegawaiPribadi.objects.filter(id=id_pegawaipribadi)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipribadi')

#pegawaipekerjaan
def pegawaipekerjaan(request):
    pegawai = PegawaiPekerjaan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaipekerjaan.html', kontext)

def detail_pegawai_pekerjaan(request):
    pegawai = PegawaiPekerjaan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawaipekerjaan.html', kontext)

def tambah_pegawai_pekerjaan(request):
    if request.method == 'POST':
        form = PegawaiPekerjaanForm(request.POST)
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

def ubah_pegawai_pekerjaan(request, id_pegawaipekerjaan):
    pegawai = PegawaiPekerjaan.objects.get(id=id_pegawaipekerjaan)
    if request.method == 'POST':
        form = PegawaiPekerjaanForm(request.POST, instance=pegawai)
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

def hapus_pegawai_pekerjaan(request, id_pegawaipekerjaan):
   pegawai = PegawaiPekerjaan.objects.filter(id=id_pegawaipekerjaan)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipekerjaan')

#pegawai pendidikan
def pegawaipendidikan(request):
    pegawai = PegawaiPendidikan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaipendidikan.html', kontext)

def detail_pegawai_pendidikan(request):
    pegawai = PegawaiPendidikan.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawai-pendidikan.html', kontext)

def tambah_pegawai_pendidikan(request):
    if request.method == 'POST':
        form = PegawaiPendidikanForm(request.POST)
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

def ubah_pegawai_pendidikan(request, id_pegawaipendidikan):
    pegawai = PegawaiPendidikan.objects.get(id=id_pegawaipendidikan)
    if request.method == 'POST':
        form = PegawaiPendidikanForm(request.POST, instance=pegawai)
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

def hapus_pegawai_pendidikan(request, id_pegawaipendidikan):
   pegawai = PegawaiPendidikan.objects.filter(id=id_pegawaipendidikan)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaipendidikan')

# pegawai keluarga
def pegawaikeluarga(request):
    pegawai = PegawaiKeluarga.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaikeluarga.html', kontext)

def detail_pegawai_keluarga(request):
    pegawai = PegawaiKeluarga.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawai-keluarga.html', kontext)

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

def hapus_pegawai_keluarga(request, id_pegawaikeluarga):
   pegawai = PegawaiKeluarga.objects.filter(id=id_pegawaikeluarga)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaikeluarga')

#pegawai bank

def pegawaibank(request):
    pegawai = PegawaiBank.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'pegawaibank.html', kontext)

def detail_pegawai_bank(request):
    pegawai = PegawaiBank.objects.all()
    kontext = {
        'pegawai' : pegawai,
        
    }

    return render(request, 'detail-pegawai-bank.html', kontext)

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

def hapus_pegawai_bank(request, id_pegawaibank):
   pegawai = PegawaiBank.objects.filter(id=id_pegawaibank)
   pegawai.delete()

   messages.success(request, "Data berhasil di hapus")

   return redirect('pegawaibank')

