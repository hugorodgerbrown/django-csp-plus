# Generated by Django 4.1.3 on 2022-12-03 15:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CspRule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "directive",
                    models.CharField(
                        choices=[
                            ("default-src", "default-src"),
                            ("child-src", "child-src"),
                            ("connect-src", "connect-src"),
                            ("font-src", "font-src"),
                            ("frame-src", "frame-src"),
                            ("img-src", "img-src"),
                            ("manifest-src", "manifest-src"),
                            ("media-src", "media-src"),
                            ("object-src", "object-src"),
                            ("prefetch-src", "prefetch-src"),
                            ("script-src", "script-src"),
                            ("script-src-elem", "script-src-elem"),
                            ("script-src-attr", "script-src-attr"),
                            ("style-src", "style-src"),
                            ("style-src-elem", "style-src-elem"),
                            ("style-src-attr", "style-src-attr"),
                            ("worker-src", "worker-src"),
                        ],
                        max_length=50,
                    ),
                ),
                ("value", models.CharField(max_length=255)),
                ("enabled", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "CSP Rule",
                "ordering": ["directive", "value"],
                "unique_together": {("value", "directive")},
            },
        ),
        migrations.CreateModel(
            name="CspReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("document_uri", models.URLField()),
                ("effective_directive", models.TextField()),
                ("disposition", models.CharField(max_length=12)),
                ("blocked_uri", models.URLField()),
                ("request_count", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "last_updated_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
            options={
                "verbose_name": "CSP Violation",
                "ordering": ["effective_directive", "blocked_uri"],
                "unique_together": {("effective_directive", "blocked_uri")},
            },
        ),
    ]
