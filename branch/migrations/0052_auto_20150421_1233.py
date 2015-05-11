# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0051_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='banned',
            field=models.ManyToManyField(verbose_name='Membres bannis', blank=True, to=settings.AUTH_USER_MODEL, related_name='banned_users', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='creator',
            field=models.ForeignKey(verbose_name='Créateur de la branche', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='location',
            field=models.CharField(verbose_name='Adresse', blank=True, max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, verbose_name='Membres de la branche', through='branch.BranchMembers', to=settings.AUTH_USER_MODEL, related_name='members'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(verbose_name='Nom de la branche', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branchmembers',
            name='joined',
            field=models.DateTimeField(verbose_name="date d'arrivé"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Commentez'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='branch',
            field=models.ForeignKey(verbose_name='Branche', to='branch.Branch', related_name='demand_branch'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name="Type d'aide", max_length=21, choices=[('1', 'Visite à la maison'), ('2', 'Tenir compagnie'), ('3', 'Transport par voiture'), ('4', 'Shopping'), ('5', 'Garder des maisons'), ('6', 'Petits boulots manuels'), ('7', 'Jardinage'), ('8', 'Garder des animaux'), ('9', 'Soins personnels'), ('a', 'Administratif'), ('b', 'Autre')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='closed',
            field=models.BooleanField(verbose_name='Vontaire assigné', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='donor',
            field=models.ForeignKey(related_name='demand_donor', verbose_name='Donneur', to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='estimated_time',
            field=models.IntegerField(verbose_name='Temps estimé (en minutes)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='km',
            field=models.IntegerField(verbose_name='Distance depuis domicile', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='location',
            field=models.CharField(verbose_name='Adresse', blank=True, max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='real_time',
            field=models.IntegerField(verbose_name='Temps réel (en minutes)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='receive_help_from_who',
            field=models.IntegerField(verbose_name='Qui peut voir et répondre à la demande/offre ?', choices=[(5, 'Tous'), (3, 'Membre vérifié'), (6, 'Mes membres favoris')], default=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='receiver',
            field=models.ForeignKey(related_name='demand_receiver', verbose_name='Receveur', to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='success',
            field=models.NullBooleanField(verbose_name='Tâche finie avec succès', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='success_fill',
            field=models.BooleanField(verbose_name='Demande de confirmation envoyée', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name='Heures de disponibilité', max_length=17, help_text='Selectionnez les heures qui vous conviennent', choices=[(1, 'Début de matinée (8h-10h)'), (2, 'Fin de matinée (10h-12h)'), (3, 'Midi (12h-13h)'), (4, "Début d'après-midi (13h-16h)"), (5, "Fin d'après-midi (16h-19h)"), (6, 'Repas du soir (19h-20h)'), (7, 'Début de soirée (20h-22h)'), (8, 'Fin de soirée (22h-00h)'), (9, 'Nuit (00h-8h)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='title',
            field=models.CharField(verbose_name='Titre', max_length=120, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='accepted',
            field=models.BooleanField(verbose_name='Proposition acceptée', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='comment',
            field=models.TextField(verbose_name='Commentaire (facultatif)', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='created',
            field=models.DateTimeField(verbose_name='Date de création', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='km',
            field=models.IntegerField(verbose_name='Distance depuis domicile', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name='Heure(s) choisie(s)', max_length=17, help_text='Selectionnez les heures qui vous conviennent', choices=[(1, 'Début de matinée (8h-10h)'), (2, 'Fin de matinée (10h-12h)'), (3, 'Midi (12h-13h)'), (4, "Début d'après-midi (13h-16h)"), (5, "Fin d'après-midi (16h-19h)"), (6, 'Repas du soir (19h-20h)'), (7, 'Début de soirée (20h-22h)'), (8, 'Fin de soirée (22h-00h)'), (9, 'Nuit (00h-8h)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='branch',
            field=models.ForeignKey(verbose_name='Branche', to='branch.Branch', related_name='offer_branch'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name="Type d'aide", max_length=21, choices=[('1', 'Visite à la maison'), ('2', 'Tenir compagnie'), ('3', 'Transport par voiture'), ('4', 'Shopping'), ('5', 'Garder des maisons'), ('6', 'Petits boulots manuels'), ('7', 'Jardinage'), ('8', 'Garder des animaux'), ('9', 'Soins personnels'), ('a', 'Administratif'), ('b', 'Autre')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='donor',
            field=models.ForeignKey(related_name='offer_donor', verbose_name='Donneur', to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='receive_help_from_who',
            field=models.IntegerField(verbose_name='Qui peut voir et répondre à la demande/offre ?', choices=[(5, 'Tous'), (3, 'Membre vérifié'), (6, 'Mes membres favoris')], default=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='receiver',
            field=models.ForeignKey(related_name='offer_receiver', verbose_name='Receveur', to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name='Heures de disponibilité', max_length=17, help_text='Selectionnez les heures qui vous conviennent', choices=[(1, 'Début de matinée (8h-10h)'), (2, 'Fin de matinée (10h-12h)'), (3, 'Midi (12h-13h)'), (4, "Début d'après-midi (13h-16h)"), (5, "Fin d'après-midi (16h-19h)"), (6, 'Repas du soir (19h-20h)'), (7, 'Début de soirée (20h-22h)'), (8, 'Fin de soirée (22h-00h)'), (9, 'Nuit (00h-8h)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='comment',
            field=models.TextField(verbose_name='Commentaire', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='created',
            field=models.DateTimeField(verbose_name='Date de création', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='time',
            field=models.IntegerField(verbose_name='Temps passé (en minutes)', blank=True, null=True),
            preserve_default=True,
        ),
    ]
