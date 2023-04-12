# Generated by Django 4.1.7 on 2023-04-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_userprofile_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="address",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="birth_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="gender",
            field=models.CharField(
                choices=[("M", "男性"), ("F", "女性")], max_length=1, null=True
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="phone_number",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
