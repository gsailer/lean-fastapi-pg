# {{ cookiecutter.project_name }}

## Getting everything running

``{{ cookiecutter.project_name.upper() }}_DB_PASSWORD=password123 docker-compose up --build``

## Adding new tables

``{{ cookiecutter.project_name.upper() }}_DB_PASSWORD=password123 docker-compose run migration poetry run alembic revision -m "YOUR MSG"``

Modify the generated alembic migration code and then apply the migration. On every start of the setup all alembic migrations are applied.
