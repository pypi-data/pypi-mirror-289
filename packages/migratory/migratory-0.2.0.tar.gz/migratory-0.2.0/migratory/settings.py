from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Setting:
    database_uri: str
    migration_table: str = 'migratory'
    migration_folder: str = 'revisions'

