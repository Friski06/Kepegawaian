from import_export import resources
from import_export.fields import Field

from absen.models import Absen


class AbsenResource(resources.ModelResource):
    nama = Field(attribute='pegawaipribadi__nama', column_name='Nama')
    nip = Field(attribute='pegawaipribadi__nip', column_name='Nip')
    class Meta:
        model = Absen
        fields = ('nama', 'nip', 'tanggal', 'masuk', 'pulang', 'jumlah_jam','jumlah_potongan_tukin')

class AbsenUserResource(resources.ModelResource):
    nama = Field(attribute='pegawaipribadi__nama', column_name='Nama')
    nip = Field(attribute='pegawaipribadi__nip', column_name='Nip')
    class Meta:
        model = Absen
        fields = ('nama', 'nip', 'tanggal', 'masuk', 'pulang', 'jumlah_jam')        