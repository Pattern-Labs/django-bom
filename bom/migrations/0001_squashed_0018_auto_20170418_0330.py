# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 05:43
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('bom', '0001_initial'), ('bom', '0002_auto_20170222_0441'), ('bom', '0003_distributor_distributorpart'), ('bom', '0004_auto_20170309_0019'), ('bom', '0005_auto_20170309_0145'), ('bom', '0006_auto_20170415_1601'), ('bom', '0007_auto_20170415_1653'), ('bom', '0008_auto_20170415_1712'), ('bom', '0009_auto_20170415_1723'), ('bom', '0010_part_manufacturer'), ('bom', '0011_remove_part_manufacturer_name'), ('bom', '0012_auto_20170415_1821'), ('bom', '0013_auto_20170415_1823'), ('bom', '0014_remove_partfile_name'), ('bom', '0015_auto_20170415_1911'), ('bom', '0016_auto_20170417_0025'), ('bom', '0017_auto_20170417_0046'), ('bom', '0018_auto_20170418_0330')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_item', models.IntegerField(blank=True, default=None, validators=[django.core.validators.MaxValueValidator(9999)])),
                ('number_variation', models.IntegerField(blank=True, default=None, validators=[django.core.validators.MaxValueValidator(99)])),
                ('description', models.CharField(default='', max_length=255)),
                ('revision', models.CharField(default='1', max_length=2)),
                ('manufacturer_part_number', models.CharField(blank=True, default='', max_length=128)),
                ('manufacturer', models.CharField(blank=True, default='', max_length=128)),
                ('minimum_order_quantity', models.IntegerField(blank=True, null=True)),
                ('minimum_pack_quantity', models.IntegerField(blank=True, null=True)),
                ('unit_cost', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(default=None, max_length=255)),
                ('comment', models.CharField(blank=True, default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subpart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('assembly_part', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assembly_part', to='bom.Part')),
                ('assembly_subpart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assembly_subpart', to='bom.Part')),
            ],
        ),
        migrations.AddField(
            model_name='part',
            name='number_class',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='number_class', to='bom.PartClass'),
        ),
        migrations.AddField(
            model_name='part',
            name='subparts',
            field=models.ManyToManyField(blank=True, through='bom.Subpart', to=b'bom.Part'),
        ),
        migrations.AlterField(
            model_name='part',
            name='description',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='part',
            name='manufacturer',
            field=models.CharField(blank=True, default=None, max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='part',
            unique_together=set([('number_class', 'number_item', 'number_variation')]),
        ),
        migrations.AlterField(
            model_name='part',
            name='number_item',
            field=models.CharField(blank=True, default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='part',
            name='number_variation',
            field=models.CharField(blank=True, default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='part',
            name='revision',
            field=models.CharField(max_length=2),
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DistributorPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_order_quantity', models.IntegerField(blank=True, null=True)),
                ('minimum_pack_quantity', models.IntegerField(blank=True, null=True)),
                ('unit_cost', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('lead_time_days', models.IntegerField(blank=True, null=True)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Distributor')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Part')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='distributorpart',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='part',
            name='minimum_order_quantity',
        ),
        migrations.RemoveField(
            model_name='part',
            name='minimum_pack_quantity',
        ),
        migrations.RemoveField(
            model_name='part',
            name='unit_cost',
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SellerPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_order_quantity', models.IntegerField(blank=True, null=True)),
                ('minimum_pack_quantity', models.IntegerField(blank=True, null=True)),
                ('unit_cost', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('lead_time_days', models.IntegerField(blank=True, null=True)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Part')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Seller')),
                ('ncnr', models.BooleanField(default=False)),
                ('nre_cost', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sellerpart',
            unique_together=set([('seller', 'part', 'minimum_order_quantity', 'unit_cost')]),
        ),
        migrations.RemoveField(
            model_name='distributorpart',
            name='distributor',
        ),
        migrations.RemoveField(
            model_name='distributorpart',
            name='part',
        ),
        migrations.DeleteModel(
            name='Distributor',
        ),
        migrations.DeleteModel(
            name='DistributorPart',
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PartFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=128)),
                ('file', models.FileField(upload_to='partfiles/')),
                ('upload_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='part',
            old_name='manufacturer',
            new_name='manufacturer_name',
        ),
        migrations.AddField(
            model_name='partfile',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Part'),
        ),
        migrations.AddField(
            model_name='part',
            name='manufacturer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bom.Manufacturer'),
        ),
        migrations.RemoveField(
            model_name='part',
            name='manufacturer_name',
        ),
        migrations.RemoveField(
            model_name='partfile',
            name='name',
        ),
        migrations.AlterField(
            model_name='partfile',
            name='file',
            field=models.FileField(upload_to='/partfiles'),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('subscription', models.CharField(choices=[('F', 'Free'), ('P', 'Pro')], max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('A', 'Admin'), ('V', 'Viewer')], max_length=1)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='partfile',
            name='file',
            field=models.FileField(upload_to='partfiles/'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bom.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bom.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bom.Organization'),
            preserve_default=False,
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
    ]
