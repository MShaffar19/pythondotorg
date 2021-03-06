# Generated by Django 2.0.13 on 2020-10-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sponsors", "0005_auto_20201015_0908"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SponsorshipLevel", new_name="SponsorshipPackage",
        ),
        migrations.RemoveField(model_name="sponsorshipbenefit", name="levels",),
        migrations.RemoveField(model_name="sponsorshipbenefit", name="minimum_level",),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="new",
            field=models.BooleanField(
                default=False,
                help_text='If selected, display a "New This Year" badge along side the benefit.',
                verbose_name="New Benefit",
            ),
        ),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="package_only",
            field=models.BooleanField(
                default=False,
                help_text="If a benefit is only available via a sponsorship package, select this option.",
                verbose_name="Package Only Benefit",
            ),
        ),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="packages",
            field=models.ManyToManyField(
                help_text="What sponsorship packages this benefit is included in.",
                related_name="benefits",
                to="sponsors.SponsorshipPackage",
                verbose_name="Sponsorship Packages",
            ),
        ),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="soft_capacity",
            field=models.BooleanField(
                default=False,
                help_text="If a benefit's capacity is flexible, select this option.",
                verbose_name="Soft Capacity",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="internal_value",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Value used internally to calculate sponsorship value when applicants construct their own sponsorship packages.",
                null=True,
                verbose_name="Internal Value",
            ),
        ),
    ]
