# Generated by Django 3.0.8 on 2020-12-26 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person_id', models.IntegerField(blank=True, default=1)),
                ('full_name', models.CharField(max_length=100)),
                ('full_name_romanized', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=None, max_length=1)),
                ('photo', models.ImageField(default='person/images/defaultPersonImage.jpg', max_length=200, upload_to='person/images')),
                ('birth', models.CharField(blank=True, max_length=11)),
                ('death', models.CharField(blank=True, default='Alive', max_length=11)),
                ('same_vamsha', models.BooleanField(default=True)),
                ('batch_no', models.IntegerField(blank=True, default=1, verbose_name='Pusta Number')),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
                ('spouses', models.CharField(default='No Spouse', max_length=200)),
                ('children', picklefield.fields.PickledObjectField(blank=True, editable=False, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('social_media', picklefield.fields.PickledObjectField(blank=True, editable=False, null=True)),
                ('remarks', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_edited_on', models.DateTimeField(auto_now=True)),
                ('suggestions', picklefield.fields.PickledObjectField(blank=True, editable=False, null=True)),
                ('father', models.ForeignKey(blank=True, limit_choices_to={'gender': 'M'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_father', to='backend.Person', verbose_name='Father')),
                ('last_edited_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('mother', models.ForeignKey(blank=True, limit_choices_to={'gender': 'F'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_mother', to='backend.Person', verbose_name='Mother')),
            ],
        ),
    ]
