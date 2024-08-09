from django.db.utils import DatabaseError
from django.conf import settings
from django.core.management import call_command
from django.db.migrations.recorder import MigrationRecorder
from django.db import connections
from dektools.zip import compress_files, decompress_files
from dekdjtools.utils.migration import list_migrations, project_dir
from dekdjtools.management.base import CommandBasic
from dekdjselfmigration.models import MigrationRecord

try:
    from psycopg2.errors import DatabaseError as PsqlDatabaseError
except ModuleNotFoundError:
    class PsqlDatabaseError(Exception):
        pass


class Command(CommandBasic):
    def handle(self, mid: str):
        try:
            exists = MigrationRecorder.Migration.objects.filter(app=__name__.partition('.')[0]).exists()
        except (DatabaseError, PsqlDatabaseError):
            exists = False
        if not exists:
            self.do_makemigrations()
            self.do_migrate()
        if MigrationRecord.objects.filter(mid=mid).exists():
            self.do_makemigrations()
            return
        queryset = MigrationRecord.objects.order_by('-id')
        try:
            mr = queryset.first()
        except DatabaseError:
            mr = None
        if mr:
            call_command('ddtdelmigrations')
            fp_set = decompress_files(mr.content, project_dir, True)
        else:
            fp_set = set()
        self.do_makemigrations()
        root_dir, filepath_set = list_migrations()
        self.do_migrate()
        if fp_set != filepath_set:
            MigrationRecord.objects.create(mid=mid, content=compress_files(root_dir, path_set=filepath_set))
            pk_list = queryset.values_list('pk', flat=True)
            if settings.DEKDJSELFMIGRATION_UP_LIMIT:
                pk_list = pk_list[settings.DEKDJSELFMIGRATION_UP_LIMIT:]
            queryset.filter(
                pk__in=pk_list
            ).delete()

    @staticmethod
    def has_psqlextra_backend():
        return any(database for database in connections.databases.values() if "psqlextra" in database["ENGINE"])

    @classmethod
    def do_makemigrations(cls):
        call_command('pgmakemigrations' if cls.has_psqlextra_backend() else 'makemigrations')

    @staticmethod
    def do_migrate():
        for name in connections.databases:
            call_command('migrate', database=name)
