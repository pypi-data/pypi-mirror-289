import os
from dekdjtools.models.base import ModelBasic, ManagerBasic
from django.db import models
from django.utils.translation import ugettext_lazy as _
from dektools.zip import decompress_files
from dektools.file import remove_path
from dektools.num import AlignNum


class MigrationRecordManager(ManagerBasic):
    def fetch(self, path):
        remove_path(path)
        max_id_list = self.annotate(max_id=models.Max('id')).values_list('max_id', flat=True)
        if max_id_list:
            an = AlignNum.from_max(max_id_list[0])
            for mr in self.order_by('id'):
                mr.fetch(os.path.join(path, an.align(mr.id)))


class MigrationRecord(ModelBasic):
    mid = models.CharField(_('mid'), max_length=100, unique=True)
    content = models.BinaryField(verbose_name=_('数据块'))
    datetime_created = models.DateTimeField(verbose_name=_('创建时间'), auto_now_add=True)

    objects = MigrationRecordManager()

    class Meta:
        verbose_name = _('迁移记录')

    def fetch(self, path):
        return decompress_files(self.content, path)
