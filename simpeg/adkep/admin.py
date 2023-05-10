from django.contrib import admin
from adkep.models import Pegawai, Absen
# Register your models here.

class PegawaiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nrp', 'email', 'alamat', 'absen_id', 'hp', 'jabatan']
    search_fields = ['nama', 'nrp']
    list_filter = ['absen_id']
    list_per_page = 5


class AbsenAdmin(admin.ModelAdmin):
    list_display = ['status', 'keterangan']
    search_fields = ['status']
    list_per_page = 5

admin.site.register(Pegawai, PegawaiAdmin)
admin.site.register(Absen, AbsenAdmin)