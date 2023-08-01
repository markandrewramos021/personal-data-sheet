# Generated by Django 4.2.1 on 2023-06-09 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField(max_length=99, verbose_name='date_from')),
                ('date_to', models.DateTimeField(max_length=99, verbose_name='date_to')),
                ('position', models.CharField(max_length=99, verbose_name='position')),
                ('department', models.CharField(max_length=99, verbose_name='department')),
                ('monthly_salary', models.CharField(max_length=99, verbose_name='monthly_salary')),
                ('salary_grade', models.CharField(max_length=99, verbose_name='salary_grade')),
                ('status', models.CharField(max_length=99, verbose_name='status')),
                ('gov_service', models.CharField(max_length=99, verbose_name='gov_service')),
                ('authUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='voluntary_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_info', models.CharField(max_length=99, verbose_name='org_info')),
                ('date_from', models.DateTimeField(max_length=99, verbose_name='date_from')),
                ('date_to', models.DateTimeField(max_length=99, verbose_name='date_to')),
                ('work_hours', models.CharField(max_length=99, verbose_name='work_hours')),
                ('position', models.CharField(max_length=99, verbose_name='position')),
                ('authUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='references',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, max_length=99, null=True, verbose_name='name1')),
                ('name2', models.CharField(blank=True, max_length=99, null=True, verbose_name='name2')),
                ('name3', models.CharField(blank=True, max_length=99, null=True, verbose_name='name3')),
                ('address1', models.CharField(blank=True, max_length=99, null=True, verbose_name='address1')),
                ('address2', models.CharField(blank=True, max_length=99, null=True, verbose_name='address2')),
                ('address3', models.CharField(blank=True, max_length=99, null=True, verbose_name='address3')),
                ('telno1', models.CharField(blank=True, max_length=99, null=True, verbose_name='telno1')),
                ('telno2', models.CharField(blank=True, max_length=99, null=True, verbose_name='telno2')),
                ('telno3', models.CharField(blank=True, max_length=99, null=True, verbose_name='telno3')),
                ('gov_id', models.CharField(blank=True, max_length=99, null=True, verbose_name='gov_id')),
                ('license_id', models.CharField(blank=True, max_length=99, null=True, verbose_name='license_id')),
                ('date', models.DateField(blank=True, null=True, verbose_name='date')),
                ('indigenous', models.CharField(blank=True, max_length=99, null=True, verbose_name='indigenous')),
                ('indig_specify', models.CharField(blank=True, max_length=99, null=True, verbose_name='indig_specify')),
                ('disability', models.CharField(blank=True, max_length=99, null=True, verbose_name='disability')),
                ('disab_specify', models.CharField(blank=True, max_length=99, null=True, verbose_name='disab_specify')),
                ('solo_parent', models.CharField(blank=True, max_length=99, null=True, verbose_name='solo_parent')),
                ('solo_specify', models.CharField(blank=True, max_length=99, null=True, verbose_name='solo_specify')),
                ('authUser', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='personal_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ext', models.CharField(blank=True, max_length=99, null=True, verbose_name='name_ext')),
                ('surname', models.CharField(blank=True, max_length=99, null=True, verbose_name='surname')),
                ('firstname', models.CharField(blank=True, max_length=99, null=True, verbose_name='firstname')),
                ('middlename', models.CharField(blank=True, max_length=99, null=True, verbose_name='middlename')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date_of_birth')),
                ('place_of_birth', models.CharField(blank=True, max_length=99, null=True, verbose_name='place_of_birth')),
                ('sex', models.CharField(blank=True, max_length=99, null=True, verbose_name='sex')),
                ('citizenship', models.CharField(blank=True, max_length=99, null=True, verbose_name='citizenship')),
                ('civil_status', models.CharField(blank=True, max_length=99, null=True, verbose_name='civil_status')),
                ('bloodtype', models.CharField(blank=True, max_length=99, null=True, verbose_name='bloodtype')),
                ('height', models.CharField(blank=True, max_length=99, null=True, verbose_name='height')),
                ('weight', models.CharField(blank=True, max_length=99, null=True, verbose_name='weight')),
                ('gsis', models.CharField(blank=True, max_length=99, null=True, verbose_name='gsis')),
                ('agency_no', models.CharField(blank=True, max_length=99, null=True, verbose_name='agency_no')),
                ('pagibig', models.CharField(blank=True, max_length=99, null=True, verbose_name='pagibig')),
                ('philhealth', models.CharField(blank=True, max_length=99, null=True, verbose_name='philhealth')),
                ('sss', models.CharField(blank=True, max_length=99, null=True, verbose_name='sss')),
                ('tin', models.CharField(blank=True, max_length=99, null=True, verbose_name='tin')),
                ('telno', models.CharField(blank=True, max_length=99, null=True, verbose_name='telno')),
                ('mobile', models.CharField(blank=True, max_length=99, null=True, verbose_name='mobile')),
                ('email', models.EmailField(blank=True, max_length=99, null=True, verbose_name='email')),
                ('res_block', models.CharField(blank=True, max_length=99, null=True, verbose_name='res_block')),
                ('res_street', models.CharField(blank=True, max_length=99, null=True, verbose_name='res_street')),
                ('res_subd', models.CharField(blank=True, max_length=99, null=True, verbose_name='res_subd')),
                ('res_brgy', models.CharField(blank=True, max_length=99, null=True, verbose_name='res_brgy')),
                ('res_city', models.CharField(blank=True, max_length=99, null=True, verbose_name='res_city')),
                ('res_prov', models.CharField(blank=True, max_length=99, null=True, verbose_name='res_prov')),
                ('res_zip', models.CharField(blank=True, max_length=99, null=True, verbose_name='res_zip')),
                ('per_block', models.CharField(blank=True, max_length=99, null=True, verbose_name='per_block')),
                ('per_street', models.CharField(blank=True, max_length=99, null=True, verbose_name='per_street')),
                ('per_subd', models.CharField(blank=True, max_length=99, null=True, verbose_name='per_subd')),
                ('per_brgy', models.CharField(blank=True, max_length=99, null=True, verbose_name='per_brgy')),
                ('per_city', models.CharField(blank=True, max_length=99, null=True, verbose_name='per_city')),
                ('per_prov', models.CharField(blank=True, max_length=99, null=True, verbose_name='per_prov')),
                ('per_zip', models.CharField(blank=True, max_length=99, null=True, verbose_name='per_zip')),
                ('authUser', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=99, verbose_name='division')),
                ('unit', models.CharField(max_length=99, verbose_name='unit')),
                ('status', models.CharField(blank=True, default='Activated', max_length=99, verbose_name='status')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('authUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='other_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills_hobbies', models.CharField(max_length=99, verbose_name='skills_hobbies')),
                ('non_acad_recognition', models.CharField(max_length=99, verbose_name='non_acad_recognition')),
                ('membership', models.CharField(max_length=99, verbose_name='membership')),
                ('authUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='learning_development',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=99, verbose_name='title')),
                ('date_of_attendance_from', models.DateTimeField(max_length=99, verbose_name='date_of_attendance_from')),
                ('date_of_attendance_to', models.DateTimeField(max_length=99, verbose_name='date_of_attendance_to')),
                ('work_hours', models.CharField(max_length=99, verbose_name='work_hours')),
                ('type_of_ld', models.CharField(max_length=99, verbose_name='type_of_ld')),
                ('conducted', models.CharField(max_length=99, verbose_name='conducted')),
                ('authUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='family_background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spouse_surname', models.CharField(blank=True, max_length=99, null=True, verbose_name='spouse_surname')),
                ('spouse_extension', models.CharField(blank=True, max_length=99, null=True, verbose_name='spouse_extension')),
                ('spouse_firstname', models.CharField(blank=True, max_length=99, null=True, verbose_name='spouse_firstname')),
                ('spouse_middlename', models.CharField(blank=True, max_length=99, null=True, verbose_name='spouse_middlename')),
                ('occupation', models.CharField(blank=True, max_length=99, null=True, verbose_name='occupation')),
                ('employee_name', models.CharField(blank=True, max_length=99, null=True, verbose_name='employee_name')),
                ('business_address', models.CharField(blank=True, max_length=99, null=True, verbose_name='business_address')),
                ('family_telno', models.CharField(blank=True, max_length=99, null=True, verbose_name='family_telno')),
                ('father_firstname', models.CharField(blank=True, max_length=99, null=True, verbose_name='father_firstname')),
                ('father_middlename', models.CharField(blank=True, max_length=99, null=True, verbose_name='father_middlename')),
                ('father_surname', models.CharField(blank=True, max_length=99, null=True, verbose_name='father_surname')),
                ('father_extension', models.CharField(blank=True, max_length=99, null=True, verbose_name='father_extension')),
                ('mother_firstname', models.CharField(blank=True, max_length=99, null=True, verbose_name='mother_firstname')),
                ('mother_middlename', models.CharField(blank=True, max_length=99, null=True, verbose_name='mother_middlename')),
                ('mother_surname', models.CharField(blank=True, max_length=99, null=True, verbose_name='mother_surname')),
                ('authUser', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='educational_background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elem_school', models.CharField(blank=True, max_length=99, null=True, verbose_name='elem_school')),
                ('elem_course', models.CharField(blank=True, max_length=99, null=True, verbose_name='elem_course')),
                ('elem_attendance_to', models.CharField(blank=True, max_length=99, null=True, verbose_name='elem_attendance_to')),
                ('elem_attendance_from', models.CharField(blank=True, max_length=99, null=True, verbose_name='elem_attendance_from')),
                ('elem_units', models.CharField(blank=True, max_length=99, null=True, verbose_name='elem_units')),
                ('elem_grad', models.CharField(blank=True, max_length=99, null=True, verbose_name='elem_grad')),
                ('elem_honors', models.CharField(blank=True, max_length=99, null=True, verbose_name='elem_honors')),
                ('secondary_school', models.CharField(blank=True, max_length=99, null=True, verbose_name='secondary_school')),
                ('secondary_course', models.CharField(blank=True, max_length=99, null=True, verbose_name='secondary_course')),
                ('secondary_attendance_to', models.CharField(blank=True, max_length=99, null=True, verbose_name='secondary_attendance_to')),
                ('secondary_attendance_from', models.CharField(blank=True, max_length=99, null=True, verbose_name='secondary_attendance_from')),
                ('secondary_units', models.CharField(blank=True, max_length=99, null=True, verbose_name='secondary_units')),
                ('secondary_grad', models.CharField(blank=True, max_length=99, null=True, verbose_name='secondary_grad')),
                ('secondary_honors', models.CharField(blank=True, max_length=99, null=True, verbose_name='secondary_honors')),
                ('vocational_school', models.CharField(blank=True, max_length=99, null=True, verbose_name='vocational_school')),
                ('vocational_course', models.CharField(blank=True, max_length=99, null=True, verbose_name='vocational_course')),
                ('vocational_attendance_to', models.CharField(blank=True, max_length=99, null=True, verbose_name='vocational_attendance_to')),
                ('vocational_attendance_from', models.CharField(blank=True, max_length=99, null=True, verbose_name='vocational_attendance_from')),
                ('vocational_units', models.CharField(blank=True, max_length=99, null=True, verbose_name='vocational_units')),
                ('vocational_grad', models.CharField(blank=True, max_length=99, null=True, verbose_name='vocational_grad')),
                ('vocational_honors', models.CharField(blank=True, max_length=99, null=True, verbose_name='vocational_honors')),
                ('college_school', models.CharField(blank=True, max_length=99, null=True, verbose_name='college_school')),
                ('college_course', models.CharField(blank=True, max_length=99, null=True, verbose_name='college_course')),
                ('college_attendance_to', models.CharField(blank=True, max_length=99, null=True, verbose_name='college_attendance_to')),
                ('college_attendance_from', models.CharField(blank=True, max_length=99, null=True, verbose_name='college_attendance_from')),
                ('college_units', models.CharField(blank=True, max_length=99, null=True, verbose_name='college_units')),
                ('college_grad', models.CharField(blank=True, max_length=99, null=True, verbose_name='college_grad')),
                ('college_honors', models.CharField(blank=True, max_length=99, null=True, verbose_name='college_honors')),
                ('grad_school', models.CharField(blank=True, max_length=99, null=True, verbose_name='grad_school')),
                ('grad_course', models.CharField(blank=True, max_length=99, null=True, verbose_name='grad_course')),
                ('grad_attendance_to', models.CharField(blank=True, max_length=99, null=True, verbose_name='grad_attendance_to')),
                ('grad_attendance_from', models.CharField(blank=True, max_length=99, null=True, verbose_name='grad_attendance_from')),
                ('grad_units', models.CharField(blank=True, max_length=99, null=True, verbose_name='grad_units')),
                ('grad_grad', models.CharField(blank=True, max_length=99, null=True, verbose_name='grad_grad')),
                ('grad_honors', models.CharField(blank=True, max_length=99, null=True, verbose_name='grad_honors')),
                ('authUser', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='civil_service_eligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eligibility', models.CharField(blank=True, max_length=99, null=True, verbose_name='eligibility')),
                ('rating', models.CharField(blank=True, max_length=99, null=True, verbose_name='rating')),
                ('exam_date', models.DateTimeField(blank=True, null=True, verbose_name='exam_date')),
                ('exam_place', models.CharField(blank=True, max_length=99, null=True, verbose_name='exam_place')),
                ('license_number', models.CharField(blank=True, max_length=99, null=True, verbose_name='license_number')),
                ('license_validity_date', models.DateTimeField(blank=True, max_length=99, null=True, verbose_name='license_validity_date')),
                ('authUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
        migrations.CreateModel(
            name='children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=99, null=True, verbose_name='name')),
                ('date_birth', models.DateTimeField(blank=True, max_length=99, null=True, verbose_name='date_birth')),
                ('authUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authUser')),
            ],
        ),
    ]
