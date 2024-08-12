from migratory import migration
from migratory.settings import Setting


def new_migration(setting: Setting, message: str) -> None:
    migration.Migration(setting).new_migration(message)

def upgrade(setting: Setting) -> None:
    migration.Migration(setting).upgrade()

# new_migration(
#     setting=Setting(
#         migration_table="migratory",
#         migration_folder="migrations",
#         database_uri="crate://localhost:4200",
#     ),
#     message="t2",
# )
upgrade(
    setting=Setting(
        migration_table="migratory",
        migration_folder="migrations",
        database_uri="crate://localhost:4200",
    ),
)
