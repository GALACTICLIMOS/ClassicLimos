# Generated by Django 4.2.5 on 2023-10-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RESERVATION_FORM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('phone_num', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('pick_up_address', models.CharField(max_length=100, null=True)),
                ('drop_off_Address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('zipcode', models.CharField(max_length=30, null=True)),
                ('pick_up_Date', models.CharField(max_length=30, null=True)),
                ('pick_Up_Time', models.CharField(max_length=30, null=True)),
                ('stop_En_Route', models.CharField(max_length=100, null=True)),
                ('number_of_Hours', models.IntegerField(null=True)),
                ('no_of_Passengers', models.IntegerField(null=True)),
                ('select_Vehicle', models.CharField(max_length=30, null=True)),
                ('routing_Request', models.CharField(max_length=100, null=True)),
                ('first_Name_credit_card', models.CharField(max_length=30, null=True)),
                ('last_Name_credit_card', models.CharField(max_length=30, null=True)),
                ('credit_card_Number', models.CharField(max_length=30, null=True)),
                ('month_Year', models.CharField(max_length=30, null=True)),
                ('Digit3_cvvifAMEX', models.CharField(max_length=100, null=True)),
                ('Billing_email', models.EmailField(max_length=100, null=True)),
                ('billing_Address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
