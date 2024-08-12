import logging
import os
from dataclasses import dataclass

import sqlalchemy as sa
import yaml
from migratory import settings


@dataclass(slots=True, frozen=True)
class Revision:
    revision: int
    message: str
    upgrade: list[str]
    downgrade: list[str]


class Migration:
    logger = logging.getLogger("migration")

    def __init__(self, setting: settings.Setting) -> None:
        self.setting = setting

    def new_migration(self, message: str):
        logger = logging.getLogger("new-migration")
        os.makedirs(self.setting.migration_folder, exist_ok=True)
        logger.info("new migration %s", message)
        migrations = self.get_migrations()
        if len(migrations) == 0:
            revision = 0
        else:
            revision = migrations[-1].revision + 1

        name = f"{revision:03d}_{message.replace(' ', '_')}.yaml"
        with open(os.path.join(self.setting.migration_folder, name), "w") as f:
            yaml.dump(
                {
                    "revision": revision,
                    "message": message,
                    "upgrade": [],
                    "downgrade": [],
                },
                f,
                sort_keys=False,
            )

    def get_migrations(self) -> list[Revision]:
        files = os.listdir(self.setting.migration_folder)
        result: list[Revision] = []
        for file in files:
            with open(os.path.join(self.setting.migration_folder, file), "r") as f:
                raw_migration = yaml.safe_load(f)
                result.append(Revision(**raw_migration))
        result.sort(key=lambda revision: revision.revision)
        return result

    def _get_create_migration_table_query(self) -> sa.TextClause:
        return sa.text(
            f"""
            CREATE TABLE IF NOT EXISTS {self.setting.migration_table}(
                revision INT
            );
            """
        )

    def _create_migration_table_row_query(self) -> sa.TextClause:
        return sa.text(
            f"""
            INSERT INTO {self.setting.migration_table} VALUES (-1);
            """
        )

    def _get_last_revision_query(self) -> sa.TextClause:
        return sa.text(
            f"""
            SELECT revision FROM {self.setting.migration_table};
            """
        )

    def _update_revision_table(self, revision_id: int) -> sa.TextClause:
        return sa.text(
            f"""
            UPDATE {self.setting.migration_table} SET revision={revision_id};
        """
        )

    def upgrade(self) -> None:
        engine = sa.create_engine(self.setting.database_uri, echo=True)
        with engine.connect() as connection:
            connection.execute(self._get_create_migration_table_query())
            revision_id: int | None = None
            with connection.execute(self._get_last_revision_query()) as result:
                select_result = result.mappings().fetchall()
                if len(select_result) == 1:
                    revision_id = select_result[0]["revision"]
                elif len(select_result) > 1:
                    self.logger.error("found %d revisions", len(select_result))
                    raise ValueError()
                else:
                    connection.execute(self._create_migration_table_row_query())
                    revision_id = -1
            revisions = self.get_migrations()
            for revision in revisions:
                if revision.revision <= revision_id:
                    continue
                self.logger.info("apply %d: %s", revision.revision, revision.message)
                for stm in revision.upgrade:
                    connection.execute(sa.text(stm))
                revision_id = revision.revision
                connection.execute(self._update_revision_table(revision_id))
