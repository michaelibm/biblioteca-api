from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql="CREATE EXTENSION IF NOT EXISTS unaccent;",
            reverse_sql="DROP EXTENSION IF EXISTS unaccent;",
        ),
    ]
