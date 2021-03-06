# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20141202_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comments',
            field=models.CharField(max_length=255, verbose_name='Additional comments', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='Email address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(max_length=8, choices=[('fr', 'French'), ('en', 'English'), ('nl', 'Dutch')], verbose_name='Spoken languages', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='location',
            field=models.CharField(max_length=256, verbose_name='Address', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Your phone number must be in format '+99999999'. Up to 15 digits.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number (mobile)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Your phone number must be in format '+99999999'. Up to 15 digits.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number (home)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='relationship',
            field=models.CharField(max_length=255, verbose_name='Your relationship with that person', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(max_length=8, choices=[('fr', 'French'), ('en', 'English'), ('nl', 'Dutch')], verbose_name='Spoken languages', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='location',
            field=models.CharField(max_length=256, verbose_name='Address', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='mobile_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Your phone number must be in format '+99999999'. Up to 15 digits.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number (mobile)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='order',
            field=models.IntegerField(default=0, choices=[(1, 'First contact'), (2, 'Contact'), (3, 'Last contact')], verbose_name='Priority'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Your phone number must be in format '+99999999'. Up to 15 digits.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number (home)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(verbose_name='Birthday', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='credit',
            field=models.IntegerField(default=0, verbose_name='Remaining credit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='Email address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='how_found',
            field=multiselectfield.db.fields.MultiSelectField(max_length=41, choices=[('internet', 'The Internet'), ('show', 'A presentation, brochure, flyer,... '), ('branch', 'The local branch'), ('member', 'Another member'), ('friends', 'Friends or family'), ('other', 'Other ...')], verbose_name='How did you hear about care4care ?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(max_length=8, choices=[('fr', 'French'), ('en', 'English'), ('nl', 'Dutch')], verbose_name='Spoken languages', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=256, verbose_name='Address', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Your phone number must be in format '+99999999'. Up to 15 digits.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number (mobile)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Your phone number must be in format '+99999999'. Up to 15 digits.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number (home)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, 'Active'), (2, 'On vacation'), (3, 'Disabled')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(help_text='A member can help or be helped while a non-member is a professional who registers to access patient data. Please choose the one that suits you', default=1, choices=[(1, 'Member'), (2, 'Non-member')], verbose_name='Account type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'Enter a valid username. No more than 30 characters. There may be numbers andcharacters  @/./+/-/_', 'invalid')], max_length=30, unique=True, verbose_name='Username'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifiedinformation',
            name='criminal_record',
            field=models.FileField(upload_to='documents/', verbose_name='Criminal record', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifiedinformation',
            name='recomendation_letter_1',
            field=models.FileField(upload_to='documents/', verbose_name='Letter of recommendation n°1', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifiedinformation',
            name='recomendation_letter_2',
            field=models.FileField(upload_to='documents/', verbose_name='Letter de recommendation n°2', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='additional_info',
            field=models.TextField(max_length=300, verbose_name='Additional information', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='asked_job',
            field=multiselectfield.db.fields.MultiSelectField(max_length=21, choices=[('1', 'Visit home'), ('2', 'Companionship'), ('3', 'Transport by car'), ('4', 'Shopping'), ('5', 'House sitting'), ('6', 'Manuals jobs'), ('7', 'Gardening'), ('8', 'Pet sitting'), ('9', 'Personal care'), ('a', 'Administrative'), ('b', 'Other ...')], verbose_name='What jobs you need?', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='can_wheelchair',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Can you carry a wheelchair in your car?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='drive_license',
            field=multiselectfield.db.fields.MultiSelectField(max_length=11, choices=[(1, 'Moped'), (2, 'Motorcycle'), (3, 'Car'), (4, 'Truck'), (5, 'Bus'), (6, 'Tractor')], verbose_name='Type of driving license', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='have_car',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you have a car?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='hobbies',
            field=models.TextField(max_length=200, verbose_name='Your hobby', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='mail_preferences',
            field=models.IntegerField(default=1, choices=[(1, 'Message box'), (2, 'Mail')], verbose_name='Receive my messages'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='offered_job',
            field=multiselectfield.db.fields.MultiSelectField(max_length=21, choices=[('1', 'Visit home'), ('2', 'Companionship'), ('3', 'Transport by car'), ('4', 'Shopping'), ('5', 'House sitting'), ('6', 'Manuals jobs'), ('7', 'Gardening'), ('8', 'Pet sitting'), ('9', 'Personal care'), ('a', 'Administrative'), ('b', 'Other ...')], verbose_name='What jobs you want to do?', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='receive_help_from_who',
            field=models.IntegerField(default=5, choices=[(5, 'All'), (3, 'Verified member'), (6, 'Favorites')], verbose_name='Receive offers and demands'),
            preserve_default=True,
        ),
    ]
