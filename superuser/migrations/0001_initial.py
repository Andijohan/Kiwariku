# Generated by Django 5.1.2 on 2024-10-30 09:44

import datetime
import django.db.models.deletion
import django_ckeditor_5.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('activity_date', models.DateField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Kegiatan',
            },
        ),
        migrations.CreateModel(
            name='Goverment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_pemerintah', models.ImageField(upload_to='foto_pemerintahan_desa/')),
                ('nama_orang', models.CharField(max_length=255)),
                ('jobdesk', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Pemerintahan desa',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2024, 10, 30, 16, 44, 46, 198570))),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='account_set', related_query_name='account', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='account_set', related_query_name='account', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Pengguna',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pengumuman',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255, unique=True)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Artikel',
            },
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIK', models.CharField(max_length=16, unique=True)),
                ('KK', models.CharField(max_length=16, unique=True)),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('tempat_lahir', models.CharField(max_length=255)),
                ('RT', models.IntegerField()),
                ('RW', models.IntegerField()),
                ('tanggal_lahir', models.DateField()),
                ('alamat', models.CharField(max_length=500)),
                ('agama', models.CharField(choices=[('BUDDHA', 'Buddha'), ('KRISTEN', 'Kristen'), ('ISLAM', 'Islam'), ('KATOLIK', 'Katolik'), ('HINDU', 'Hindu'), ('KONGHUCU', 'Konghucu')], max_length=255)),
                ('jenis_kelamin', models.CharField(choices=[('LAKI-LAKI', 'Laki-Laki'), ('PEREMPUAN', 'Perempuan')], max_length=255)),
                ('pendidikan', models.CharField(choices=[('TIDAK SEKOLAH', 'Tidak Sekolah'), ('SD', 'SD'), ('SMP', 'SMP'), ('SMA', 'SMA'), ('SMK', 'SMK'), ('SLTP', 'SLTP'), ('SLTA', 'SLTA'), ('D-1', 'D1'), ('D-2', 'D2'), ('D-3', 'D3'), ('D-4', 'D4'), ('S-1', 'S1'), ('S-2', 'S2'), ('S-3', 'S3')], max_length=255)),
                ('pekerjaan', models.CharField(choices=[('TIDAK BEKERJA', 'Tidak Bekerja'), ('KARYAWAN', 'Karyawan'), ('PENSIUNAN', 'Pensiunan'), ('PELAJAR/MAHASISWA', 'Pelajar/Mahasiswa'), ('MENGURUS RUMAH TANGGA', 'Mengurus Rumah Tangga'), ('ASISTEN RUMAH TANGGA', 'Asisten Rumah Tangga'), ('WIRASWASTA', 'Wiraswasta'), ('SATPAM/SECURITY', 'Satpam/Security'), ('BARBER', 'Barber'), ('MONTIR', 'Montir'), ('AHLI LAS/PANDAI BESI', 'Ahli Las/Pandai Besi'), ('BURUH', 'Buruh'), ('ABDI NEGARA', 'Abdi Negara'), ('PETUGAS KEBERSIHAN', 'Petugas Kebersihan'), ('NELAYAN', 'Nelayan'), ('PEMUKA AGAMA', 'Pemuka Agama'), ('WIRAUSAHA', 'Wirausaha'), ('SOPIR', 'Sopir'), ('PETERNAK', 'Peternak'), ('PENGRAJIN', 'Pengrajin'), ('DIGITALPRENEUR', 'Digitalpreneur'), ('ARSITEK', 'Arsitek'), ('PEKERJA KASAR', 'Pekerja Kasar'), ('TUKANG', 'Tukang')], max_length=255)),
                ('akun_layanan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Penduduk',
            },
        ),
    ]