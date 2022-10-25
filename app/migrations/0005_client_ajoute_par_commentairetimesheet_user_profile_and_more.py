# Generated by Django 4.0.3 on 2022-05-24 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_budget_temps_anuel_projet_budget_temps_annuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='ajoute_par',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentairetimesheet',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departement',
            name='ajoute_par',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enregistrementtimesheet',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projet',
            name='ajoute_par',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tache',
            name='ajoute_par',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
            preserve_default=False,
        ),
    ]
