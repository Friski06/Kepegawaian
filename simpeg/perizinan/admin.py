from django.contrib import admin
from perizinan.models import Cutiizin, Spt
# Register your models here.

class CutiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nrp', 'jabatan', 'keperluan', 'tgl_mulai', 'tgl_selesai']
    search_fields = ['nama', 'nrp']
    list_filter = ['tgl_mulai']
    list_per_page = 5


class SptAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nrp', 'jenis_kegiatan', 'tempat_kegiatan', 'tgl_mulai_kegiatan', 'tgl_selesai_kegiatan']
    search_fields = ['nama', 'nrp']
    list_filter = ['tgl_mulai_kegiatan']
    list_per_page = 5

admin.site.register(Cutiizin, CutiAdmin)
admin.site.register(Spt, SptAdmin)