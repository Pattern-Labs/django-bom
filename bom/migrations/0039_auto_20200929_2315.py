# Generated by Django 3.1 on 2020-09-29 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bom', '0038_auto_20200422_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturerpart',
            name='manufacturer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bom.manufacturer'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='part',
            name='number_class',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='number_class', to='bom.partclass'),
        ),
        migrations.AlterField(
            model_name='partrevision',
            name='assembly',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bom.assembly'),
        ),
        migrations.AlterField(
            model_name='usermeta',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bom.organization'),
        ),
    ]