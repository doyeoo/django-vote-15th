# Generated by Django 4.0.3 on 2022-05-24 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='candidate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='api.candidate'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
