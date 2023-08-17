from django.contrib import admin
from django.urls import path
from adkep.views import *
from perizinan.views import *
from penilaian.views import *
from absen.views import *
from dashboard.views import *
from login.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',dashboard, name='dashboard'),
    path('login/', user_login, name='login'),
    path('logout/', logout, name='logout_view'),
    path('register/',user_register, name='register'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('tambah-jabatan/', tambah_jabatan, name='tambah_jabatan'),
#{
    #pegawaipribadi
    path('pegawaipribadi/',pegawaipribadi, name='pegawaipribadi'),

    path('users/pegawaipribadi-user/',pegawaipribadi_user, name='user_pegawaipribadi'),
    path('users/databawahan/',pegawaibawahan, name='pegawaibawahan'),
    
    path('tambah-pegawai-pribadi/', tambah_pegawai_pribadi, name='tambah_pegawai_pribadi'),
    path('pegawaipribadi/ubah/<int:user_id>', ubah_pegawai_pribadi, name='ubah_pegawaipribadi'),
    path('pegawaipribadi/hapus/<int:user_id>', hapus_pegawai_pribadi, name='hapus_pegawaipribadi'),
    path('detail-pegawaipribadi/detail/<int:user_id>/', detail_pegawai_pribadi, name='detail_pegawaipribadi'),

    #pegawai pekerjaan
    path('pegawaipekerjaan/', pegawaipekerjaan, name='pegawaipekerjaan'),

    path('users/pegawaipekerjaan-user/', pegawaipekerjaan_user, name='user_pegawaipekerjaan'),

    path('tambah-pegawai-pekerjaan/', tambah_pegawai_pekerjaan, name='tambah_pegawai_pekerjaan'),
    path('pegawaipekerjaan/ubah/<int:user_id>', ubah_pegawai_pekerjaan, name='ubah_pegawaipekerjaan'),
    path('pegawaipekerjaan/hapus/<int:user_id>', hapus_pegawai_pekerjaan, name='hapus_pegawaipekerjaan'),
    path('detail-pegawaipekerjaan/detail/<int:user_id>/', detail_pegawai_pekerjaan, name='detail_pegawaipekerjaan'),

    #pegawai pendidikan
    path('pegawaipendidikan/', pegawaipendidikan, name='pegawaipendidikan'),

    path('users/pegawaipendidikan-user/', pegawaipendidikan_user, name='user_pegawaipendidikan'),

    path('tambah-pegawai-pendidikan/', tambah_pegawai_pendidikan, name='tambah_pegawai_pendidikan'),
    path('pegawaipendidikan/ubah/<int:user_id>', ubah_pegawai_pendidikan, name='ubah_pegawaipendidikan'),
    path('pegawaipendidikan/hapus/<int:user_id>', hapus_pegawai_pendidikan, name='hapus_pegawaipendidikan'),
    path('detail-pegawaipendidikan/detail/<int:pegawaipribadi_id>/', detail_pegawai_pendidikan, name='detail_pegawaipendidikan'),

    #pegawai kelaurga
    path('pegawaikeluarga/', pegawaikeluarga, name='pegawaikeluarga'),

    path('users/pegawaikeluarga-user/', pegawaikeluarga_user, name='user_pegawaikeluarga'),

    path('tambah-pegawai-keluarga/', tambah_pegawai_keluarga, name='tambah_pegawai_keluarga'),
    path('pegawaikeluarga/ubah/<int:user_id>', ubah_pegawai_keluarga, name='ubah_pegawaikeluarga'),
    path('pegawaikeluarga/hapus/<int:user_id>', hapus_pegawai_keluarga, name='hapus_pegawaikeluarga'),
    path('detail-pegawaikeluarga/detail/<int:user_id>/', detail_pegawai_keluarga, name='detail_pegawaikeluarga'),

    #pegawai bank
    path('pegawaibank/', pegawaibank, name='pegawaibank'),

    path('users/pegawaibank-user/', pegawaibank_user, name='user_pegawaibank'),

    path('tambah-pegawai-bank/', tambah_pegawai_bank, name='tambah_pegawai_bank'),
    path('pegawaibank/ubah/<int:id_pegawaibank>', ubah_pegawai_bank, name='ubah_pegawaibank'),
    path('pegawaibank/hapus/<int:id_pegawaibank>', hapus_pegawai_bank, name='hapus_pegawaibank'),
#}
#{
    #absen
    path('absen-user/', notifikasi_absen, name='notifikasi_absen'),
    path('setuju-absen/<int:id_absen>/', setuju_absen, name='setuju_absen'),
    path('tolak-absen/<int:id_absen>/', tolak_absen, name='tolak_absen'),
    path('lupaabsen/', lupaabsen, name='lupaabsen'),
    path('absen/', absen, name='absen'),
    path('absen_bawahan/', absen_bawahan, name='absen_bawahan'),
    path('users/absen/', absen_user, name='absen_user'),
    path('detailabsen/<int:pegawaipribadi_id>', detail_absen, name='detailabsen'),
    path('rekap_absen_bulanan/', rekap_absen_bulanan, name='rekapabsen'),
    path('users/rekap_absen_user/', rekap_absen_user, name='rekapabsen_user'),
    path('cetak_absen/', cetak_rekap_absen, name='cetak_absen'),
    path('cetak_absen_pdf/', cetak_rekap_absen_pdf, name='cetak_absen_pdf'),
    path('cetak_absen_pdf/', cetak_rekap_absen_user_pdf, name='cetak_absen_user_pdf'),
# }

    #linkcutiizin&spt

    path('users/cutiizin-user/', cuti_user, name='user_cutiizin'),
    path('cutiizin-user/', notifikasi, name='notifikasi'),
    path('setuju-cuti/<int:id_cuti>/', setuju_cuti, name='setuju_cuti'),
    path('cutiizin/', cutiizin, name='cutiizin'),
    path('users/sp-usert/', spt_user, name='user_spt'),
    path('spt/', spt, name='spt'),
    path('spt-user/', notifikasi_spt, name='notifikasi_spt'),
    path('setuju-spt/<int:id_spt>/', setuju_spt, name='setuju_spt'),
    path('tolak-spt/<int:id_spt>/', tolak_spt, name='tolak_spt'),
    path('tambah-cutiizin/', tambah_cutiizin,name='tambah_cutiizin'),
    path('tambah-spt/', tambah_spt,name='tambah_spt'),
    path('cuti/ubah/<int:id_cuti>', ubah_cuti, name='ubah_cuti'),
    path('spt/ubah/<int:id_spt>', ubah_spt, name='ubah_spt'),
    path('cuti/hapus/<int:id_cuti>', hapus_cuti, name='hapus_cuti'),
    path('spt/hapus/<int:id_spt>', hapus_spt, name='hapus_spt'),
    path('detailcuti/<int:pegawaipribadi_id>', detail_cuti, name='detailcuti'),
    path('cetak_cuti/', cetak_rekap_cuti, name='cetak_cuti'),
    path('cetak_cuti_pdf/', cetak_rekap_cuti_pdf, name='cetak_cuti_pdf'),
    

    #penilaian
    path('users/nilai-user/', nilai_user, name='nilai_user'),
    path('nilai/', nilai, name='nilai'),
    path('detail_nilai/<int:pegawaipribadi_id>', detail_nilai, name='detail_nilai'),
     path('detail_nilai/<int:pegawaipribadi_id>', detail_nilai_user, name='detail_nilai_user'),
    path('tambah-nilai/<int:pegawaipribadi_id>', tambah_penilaian,name='tambah_nilai'),
    path('tolakukur/', tolakukur, name='tolakukur'),
    path('cetak_nilai/', cetak_nilai, name='cetak_nilai'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)