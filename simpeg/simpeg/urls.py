
from django.contrib import admin
from django.urls import path
from adkep.views import *
from perizinan.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('datapegawai/', datapegawai, name='datapegawai'),
    path('dataabsen/', dataabsen, name='dataabsen'),
    path('tambah-pegawai/', tambah_pegawai,name='tambah_pegawai'),
    path('pegawai/ubah/<int:id_pegawai>', ubah_pegawai, name='ubah_pegawai'),
    path('pegawai/hapus/<int:id_pegawai>', hapus_pegawai, name='hapus_pegawai'),
    path('tambah-absen/', tambah_absen, name='tambah_absen'),
    path('absen/ubah/<int:id_absen>', ubah_absen, name='ubah_absen'),
    path('absen/hapus/<int:id_absen>', hapus_absen, name='hapus_absen'),

    path('cutiizin/', cutiizin, name='cutiizin'),
    path('spt/', spt, name='spt'),
    path('tambah-cutiizin/', tambah_cutiizin,name='tambah_cutiizin'),
    path('tambah-spt/', tambah_spt,name='tambah_spt'),
    path('cuti/ubah/<int:id_cuti>', ubah_cuti, name='ubah_cuti'),
    path('spt/ubah/<int:id_spt>', ubah_spt, name='ubah_spt'),
    path('cuti/hapus/<int:id_cuti>', hapus_cuti, name='hapus_cuti'),
    path('spt/hapus/<int:id_spt>', hapus_spt, name='hapus_spt'),

]
