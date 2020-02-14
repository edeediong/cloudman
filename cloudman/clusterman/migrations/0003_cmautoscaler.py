# Generated by Django 2.2.10 on 2020-02-10 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djcloudbridge', '0001_initial'),
        ('clusterman', '0002_create_rancher_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMAutoScaler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('instance_type', models.CharField(max_length=200)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autoscaler_list', to='clusterman.CMCluster')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autoscaler_list', to='djcloudbridge.Zone')),
            ],
            options={
                'verbose_name': 'Cluster Autoscaler',
                'verbose_name_plural': 'Cluster Autoscalers',
            },
        ),
    ]