# Generated by Django 3.1.7 on 2021-02-23 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('timestamp', models.TimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('done', 'Done'), ('invalid', 'Invalid')], default='new', max_length=20)),
                ('completed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_assigned', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
