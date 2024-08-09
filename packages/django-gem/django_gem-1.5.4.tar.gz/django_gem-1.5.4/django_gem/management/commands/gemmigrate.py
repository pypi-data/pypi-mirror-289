import json
from pathlib import Path

from django.apps import apps
from django.core.management import BaseCommand
from django.db import DEFAULT_DB_ALIAS, connections

from django_gem.toolkit.gem_migration.constants import (
    GEM_MIGRATIONS_STABLE_INDEX_FILE_NAME,
)
from django_gem.toolkit.gem_migration.loader import Loader
from django_gem.toolkit.gem_migration.recorder import GemMigrationRecorder
from django_gem.toolkit.saw import Saw


class Command(BaseCommand):
    def handle(self, *args, **options):
        connection = connections[DEFAULT_DB_ALIAS]
        connection.prepare_database()
        recorder = GemMigrationRecorder(connection)
        loader = Loader()
        applied_gem_migrations = recorder.applied_migrations()
        for app in apps.get_app_configs():
            if (gem_migrations_path := loader.disk_migrations_locations.get(app.label)) is None:
                continue
            gem_migrations_module = Path(gem_migrations_path)

            migration_file_names = sorted(
                [
                    migration_file.name
                    for migration_file in gem_migrations_module.glob("*.json")
                    if migration_file.name != GEM_MIGRATIONS_STABLE_INDEX_FILE_NAME
                ]
            )
            applied_migrations_count = 0
            for migration_file_name in migration_file_names:
                if (app.label, migration_file_name) not in applied_gem_migrations:
                    migration = json.loads(
                        (gem_migrations_module / migration_file_name).read_text()
                    )
                    for natural_key, field_names in migration.items():
                        Saw.cut_content_type(natural_key=natural_key, field_names=field_names)
                    recorder.record_applied(app.label, migration_file_name)
                    self.stdout.write(
                        f"Applying migration {migration_file_name} for {app.label}",
                    )
                    applied_migrations_count += 1

            if applied_migrations_count:
                self.stdout.write(f"All {applied_migrations_count} migration(s) were applied")
            else:
                self.stdout.write("No migrations to apply")
