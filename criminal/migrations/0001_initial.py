# Generated by Django 2.2.5 on 2019-10-28 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=12, null=True)),
                ('street', models.CharField(db_index=True, max_length=30, null=True)),
                ('state', models.CharField(max_length=4, null=True)),
                ('city', models.CharField(max_length=24, null=True)),
                ('unit', models.CharField(max_length=8, null=True)),
                ('zip', models.PositiveIntegerField(db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.PositiveIntegerField(unique=True)),
                ('full_name', models.CharField(db_index=True, max_length=42)),
                ('sex', models.CharField(max_length=3, null=True)),
                ('birthdate', models.DateField(db_index=True, null=True)),
                ('location', models.CharField(max_length=4, null=True)),
                ('race', models.CharField(max_length=3, null=True)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='criminal.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cause', models.CharField(max_length=22, null=True)),
                ('case_date', models.DateField(null=True)),
                ('court', models.CharField(max_length=6, null=True)),
                ('complaint_date', models.DateField(db_index=True, null=True)),
                ('offense_date', models.DateField(db_index=True, null=True)),
                ('court_date', models.DateField(db_index=True, null=True)),
                ('court_type', models.CharField(max_length=3, null=True)),
                ('offense_desc', models.CharField(db_index=True, max_length=32, null=True)),
                ('offense_code', models.PositiveIntegerField(null=True)),
                ('offense_type', models.CharField(max_length=4, null=True)),
                ('court_cost', models.FloatField(null=True)),
                ('custody_date', models.DateField(null=True)),
                ('fine_amount', models.FloatField(null=True)),
                ('case_desc', models.CharField(max_length=20, null=True)),
                ('judgement_code', models.PositiveIntegerField(null=True)),
                ('judgement_date', models.DateField(null=True)),
                ('judgment_desc', models.CharField(max_length=20, null=True)),
                ('judgement_number', models.PositiveIntegerField(null=True)),
                ('disposition_code', models.PositiveIntegerField(null=True)),
                ('disposition_date', models.DateField(null=True)),
                ('disposition_desc', models.CharField(max_length=20, null=True)),
                ('grand_jury_date', models.DateField(null=True)),
                ('grand_jury_status', models.CharField(max_length=5, null=True)),
                ('intake_prosecutor', models.CharField(max_length=32, null=True)),
                ('outtake_prosecutor', models.CharField(max_length=32, null=True)),
                ('revocation_prosecutor', models.CharField(max_length=32, null=True)),
                ('probation_prosecutor', models.CharField(max_length=32, null=True)),
                ('reduced_offense_code', models.PositiveIntegerField(null=True)),
                ('reduced_offense_desc', models.CharField(max_length=32, null=True)),
                ('reduced_offense_type', models.CharField(max_length=4, null=True)),
                ('sentence', models.CharField(max_length=12, null=True)),
                ('original_sentence', models.CharField(max_length=22, null=True)),
                ('sentence_desc', models.CharField(max_length=25, null=True)),
                ('sentence_start_date', models.DateField(null=True)),
                ('sentence_end_date', models.DateField(null=True)),
                ('setting_date', models.DateField(null=True)),
                ('setting_type', models.CharField(max_length=3, null=True)),
                ('post_judicial_date', models.DateField(null=True)),
                ('post_judicial_field', models.CharField(max_length=21, null=True)),
                ('bond_amount', models.FloatField(null=True)),
                ('bond_date', models.DateField(null=True)),
                ('bond_status', models.CharField(max_length=5, null=True)),
                ('bondsman_name', models.CharField(db_index=True, max_length=32, null=True)),
                ('attorney_name', models.CharField(db_index=True, max_length=32, null=True)),
                ('attorney_appointed_retained', models.CharField(max_length=3, null=True)),
                ('attorney_bar_nbr', models.PositiveIntegerField(db_index=True, null=True)),
                ('criminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminal.Criminal')),
            ],
        ),
    ]
