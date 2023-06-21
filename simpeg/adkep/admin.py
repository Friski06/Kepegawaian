from django.contrib import admin

# Register your models here.
from .models import JabatanStruktural, PegawaiPribadi, PegawaiPekerjaan, PegawaiPendidikan, PegawaiKeluarga, PegawaiBank, Provinsi, Kabupaten

admin.site.register(JabatanStruktural)
admin.site.register(PegawaiPribadi)
admin.site.register(PegawaiPekerjaan)
admin.site.register(PegawaiPendidikan)
admin.site.register(PegawaiKeluarga)
admin.site.register(PegawaiBank)
admin.site.register(Provinsi)
admin.site.register(Kabupaten)
