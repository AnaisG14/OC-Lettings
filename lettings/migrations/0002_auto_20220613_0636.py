# Generated by Django 3.0 on 2022-06-13 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
                INSERT INTO lettings_letting (
                    id,
                    title,
                    address_id
                )
                SELECT
                    id,
                    title,
                    address_id
                FROM
                    oc_lettings_site_letting;
            """, reverse_sql="""
                INSERT INTO oc_lettings_site_letting (
                    id,
                    title,
                    address_id
                )
                SELECT
                    id,
                    title,
                    address_id
                FROM
                    lettings_letting;
            """),
        migrations.RunSQL("""
                    INSERT INTO lettings_address (
                        id,
                        number,
                        street,
                        city,
                        state,
                        zip_code,
                        country_iso_code
                    )
                    SELECT
                        id,
                        number,
                        street,
                        city,
                        state,
                        zip_code,
                        country_iso_code
                    FROM
                        oc_lettings_site_address;
                    # SELECT setval(pg_get_serial_sequence('"lettings_lettings"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lettings_letting";
                """, reverse_sql="""
                    INSERT INTO oc_lettings_site_address (
                        id,
                        number,
                        street,
                        city,
                        state,
                        zip_code,
                        country_iso_code
                    )
                    SELECT
                        id,
                        number,
                        street,
                        city,
                        state,
                        zip_code,
                        country_iso_code
                    FROM
                        lettings_address;
                    # SELECT setval(pg_get_serial_sequence('"lettings_address"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "lettings_address";
                """)

    ]
