from migratory import migration
from migratory.settings import Setting


def new_migration(setting: Setting, message: str) -> None:
    migration.Migration(setting).new_migration(message)


def upgrade(setting: Setting) -> None:
    migration.Migration(setting).upgrade()
