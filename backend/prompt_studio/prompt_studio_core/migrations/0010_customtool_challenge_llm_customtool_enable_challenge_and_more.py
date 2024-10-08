# Generated by Django 4.2.1 on 2024-03-24 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "adapter_processor",
            "0007_remove_adapterinstance_is_default_userdefaultadapter",
        ),
        (
            "prompt_studio_core",
            "0009_customtool_single_pass_extraction_mode_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="customtool",
            name="challenge_llm",
            field=models.ForeignKey(
                blank=True,
                db_comment="Field to store challenge llm",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="challenge_customtools",
                to="adapter_processor.adapterinstance",
            ),
        ),
        migrations.AddField(
            model_name="customtool",
            name="enable_challenge",
            field=models.BooleanField(
                db_comment="Flag to enable or disable challenge", default=False
            ),
        ),
        migrations.AlterField(
            model_name="customtool",
            name="monitor_llm",
            field=models.ForeignKey(
                blank=True,
                db_comment="Field to store monitor llm",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="monitor_customtools",
                to="adapter_processor.adapterinstance",
            ),
        ),
        migrations.AlterField(
            model_name="customtool",
            name="single_pass_extraction_mode",
            field=models.BooleanField(
                db_comment="Flag to enable or disable single pass extraction mode",
                default=False,
            ),
        ),
    ]
