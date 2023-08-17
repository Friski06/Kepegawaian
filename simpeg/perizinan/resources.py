from import_export import resources
from import_export.fields import Field

from perizinan.models import Cutiizin


class CutiResource(resources.ModelResource):
    nama = Field(attribute='pegawaipribadi__nama', column_name='Nama')
    nip = Field(attribute='pegawaipribadi__nip', column_name='Nip')
    class Meta:
        model = Cutiizin
        fields = ('nama', 'nip', 'tanggal', 'masuk', 'pulang', 'jumlah_jam')