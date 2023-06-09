# Generated by Django 4.2 on 2023-06-02 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_order_alter_students_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=15, null=True)),
                ('order_price', models.IntegerField(blank=True, max_length=15, null=True)),
                ('order_discount', models.IntegerField(blank=True, max_length=5, null=True)),
                ('order_quantity', models.IntegerField(blank=True, max_length=100, null=True)),
                ('order_address', models.TextField(blank=True, max_length=100, null=True)),
                ('order_place_at', models.DateTimeField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentsAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('house_no', models.IntegerField(blank=True, max_length=5, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=12, null=True)),
                ('pincode', models.IntegerField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='mobile',
            new_name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='students',
            name='GENDER_TYPES',
        ),
        migrations.AlterField(
            model_name='students',
            name='date_of_birth',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='studentsaddress',
            name='students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_address', to='users.students'),
        ),
        migrations.AddField(
            model_name='students',
            name='gender_types',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=2),
            preserve_default=False,
        ),
    ]
