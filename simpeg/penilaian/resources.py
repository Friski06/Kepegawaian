from import_export import resources
from import_export.fields import Field

from penilaian.models import Nilai


class NilaiResource(resources.ModelResource):
    nama = Field(attribute='pegawaipribadi__nama', column_name='Nama')
    class Meta:
        model = Nilai
        fields = ('nama','rata_rata','nilai_huruf')